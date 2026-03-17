#!/usr/bin/env python3
"""
QA/Test Automation Job Scraper — Sydney NSW
Uses Google Search + open APIs (Remotive, Jobicy, Arbeitnow)
Sends Excel report via Gmail daily at 7:00 AM AEST
"""

import os, re, time, datetime, smtplib, urllib.parse, json, html
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

import requests
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# ═══════════════════════════════════════════════════
#  ★  CONFIG — ONLY EDIT THIS SECTION  ★
# ═══════════════════════════════════════════════════
RECIPIENT_EMAIL = "hvkarunakar@gmail.com"
SENDER_EMAIL    = "karunakarhv@gmail.com"
SENDER_PASSWORD = "roldrybcqvqizzsz"
# Get App Password: https://myaccount.google.com/apppasswords
# Steps: Sign into karunakarhv@gmail.com → Security → 2-Step ON
#        → App Passwords → Name it 'QA Job Tracker' → Generate
#        → Copy 16 chars (no spaces) → paste above
# ═══════════════════════════════════════════════════

SALARY_MIN = 140000
SALARY_MAX = 160000
LOCATION   = "Sydney NSW"
TODAY_STR  = datetime.date.today().strftime("%d %b %Y")
DATE_TAG   = datetime.date.today().strftime("%Y-%m-%d")

SECTORS = {
    "Insurance":            ["insurance","insurer","underwriting","claims","icare","allianz","qbe","suncorp","nib","medibank","zurich","aig"],
    "Workforce Management": ["workforce management","humanforce","deputy","kronos","ukg","scheduling","rostering","workforce","timekeeper"],
    "Rail":                 ["rail","railway","train","rolling stock","wabtec","alstom","bombardier","metro","transport for nsw","sydney trains"],
    "Defence":              ["defence","defense","military","droneshield","qinetiq","anduril","dewc","fivecast","thales","bae systems","leidos"],
    "Air":                  ["aviation","aerospace","airspace","uav","drone","unmanned aerial","airservices","boeing","airbus","casa"],
    "Embedded Systems":     ["embedded","firmware","rtos","iot","microcontroller","fpga","systems software","neara","hardware","c++","real-time"],
}

SECTOR_COLORS = {
    "Insurance":            "1F6AA5",
    "Workforce Management": "2E7D32",
    "Rail":                 "6A1B9A",
    "Defence":              "B71C1C",
    "Air":                  "00838F",
    "Embedded Systems":     "E65100",
}

QA_KEYWORDS = [
    "qa automation","test automation","sdet","software development engineer in test",
    "quality assurance engineer","automation tester","automation engineer",
    "performance test","mobile automation","test automation developer",
    "senior test","qa engineer","software tester","test engineer",
    "software quality","quality engineer","manual test","automated test",
    "test lead","testing engineer","test analyst","selenium","playwright","cypress","appium",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,*/*",
    "Accept-Language": "en-AU,en;q=0.9",
}

SESSION = requests.Session()
SESSION.headers.update(HEADERS)

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

def fetch_json(url, timeout=20):
    try:
        r = SESSION.get(url, timeout=timeout)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"  [fetch_json] {url[:70]} → {e}")
        return None

def fetch_text(url, timeout=20):
    try:
        r = SESSION.get(url, timeout=timeout)
        return r.text
    except Exception as e:
        print(f"  [fetch_text] {url[:70]} → {e}")
        return None

def strip_html(text):
    return re.sub(r"<[^>]+>", " ", html.unescape(text or "")).strip()

def extract_salary(text):
    if not text:
        return "Not listed"
    for pat in [r"\$\s*1[4-6]\d[,\s]?\d{3}", r"\$\s*\d{3}[,\s]?\d{3}",
                r"\$\d{2,3}[kK]", r"\d{3},\d{3}\s*(?:per annum|pa|p\.a\.|/yr|AUD)",
                r"\$\d{3,4}/(?:day|hr|hour)", r"\d{2,3}k\s*[-–]\s*\d{2,3}k"]:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            return m.group(0)
    return "Not listed"

def is_qa_role(title, snippet=""):
    text = (title + " " + snippet).lower()
    return any(kw in text for kw in QA_KEYWORDS)

def classify_sector(title, company, snippet):
    text = (title + " " + company + " " + snippet).lower()
    scores = {s: sum(1 for kw in kws if kw.lower() in text) for s, kws in SECTORS.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else None

def make_job(source, title, company, location, salary, job_type, link, snippet=""):
    return {"source": source, "title": title.strip(), "company": company.strip() or "N/A",
            "location": location.strip() or LOCATION, "salary": salary or "Not listed",
            "type": job_type or "Not listed", "link": link.strip(),
            "snippet": strip_html(snippet)[:200]}

def deduplicate(jobs):
    seen, out = set(), []
    for j in jobs:
        key = (j["title"].lower()[:35], j["company"].lower()[:25])
        if key not in seen:
            seen.add(key)
            out.append(j)
    return out

# ─────────────────────────────────────────────
# SOURCES
# ─────────────────────────────────────────────

def scrape_remotive():
    results = []
    print("  📡 Remotive API...")
    data = fetch_json("https://remotive.com/api/remote-jobs?category=qa&limit=100")
    if data:
        for j in data.get("jobs", []):
            if is_qa_role(j.get("title","")):
                results.append(make_job("Remotive", j.get("title",""), j.get("company_name",""),
                    "Remote (Australia-eligible)", j.get("salary","") or extract_salary(j.get("description","")),
                    "Remote", j.get("url","https://remotive.com/remote-jobs/qa"), j.get("description","")))
    print(f"     → {len(results)} QA roles")
    return results

def scrape_jobicy():
    results = []
    print("  📡 Jobicy API...")
    data = fetch_json("https://jobicy.com/api/v2/remote-jobs?count=50&tag=qa")
    if data:
        for j in data.get("jobs", []):
            if is_qa_role(j.get("jobTitle",""), j.get("jobDescription","")):
                sal_min = j.get("annualSalaryMin")
                sal_max = j.get("annualSalaryMax")
                salary  = f"${sal_min:,}–${sal_max:,}" if sal_min and sal_max else "Not listed"
                results.append(make_job("Jobicy", j.get("jobTitle",""), j.get("companyName",""),
                    "Remote (Worldwide)", salary, "Remote", j.get("url","https://jobicy.com"), j.get("jobDescription","")))
    print(f"     → {len(results)} QA roles")
    return results

def scrape_arbeitnow():
    results = []
    print("  📡 Arbeitnow API...")
    for search in ["qa automation", "test automation", "sdet"]:
        q = urllib.parse.quote_plus(search)
        data = fetch_json(f"https://www.arbeitnow.com/api/job-board-api?search={q}&location=australia")
        if data:
            for j in data.get("data", []):
                if is_qa_role(j.get("title",""), j.get("description","")):
                    results.append(make_job("Arbeitnow", j.get("title",""), j.get("company_name",""),
                        j.get("location","Remote/AU"), extract_salary(j.get("description","")),
                        "Remote" if j.get("remote") else "Onsite",
                        j.get("url","https://www.arbeitnow.com"), j.get("description","")))
        time.sleep(0.8)
    results = deduplicate(results)
    print(f"     → {len(results)} QA roles")
    return results

def google_search_jobs(site, title_query, extra=""):
    results = []
    q = urllib.parse.quote_plus(f'site:{site} "{title_query}" "Sydney" "NSW" {extra}')
    url = f"https://www.google.com/search?q={q}&num=10&hl=en-AU&gl=au"
    text = fetch_text(url)
    if not text:
        return results
    links    = re.findall(rf'href="(https://{re.escape(site)}/[^"]+)"', text)
    titles   = re.findall(r'<h3[^>]*>(.*?)</h3>', text)
    snippets = re.findall(r'<div class="[^"]*VwiC3b[^"]*"[^>]*>(.*?)</div>', text, re.DOTALL)
    src_map  = {"seek.com.au":"SEEK","au.indeed.com":"Indeed","linkedin.com":"LinkedIn","glassdoor.com.au":"Glassdoor"}
    source   = next((v for k,v in src_map.items() if k in site), "Other")
    for i, link in enumerate(links[:8]):
        raw_title = strip_html(titles[i]) if i < len(titles) else title_query
        snippet   = strip_html(snippets[i]) if i < len(snippets) else ""
        if not is_qa_role(raw_title, snippet):
            continue
        company = "See listing"
        for sep in [" at ", " - ", " | "]:
            if sep in raw_title:
                parts = raw_title.split(sep, 1) if sep == " at " else raw_title.rsplit(sep, 1)
                raw_title, company = parts[0].strip(), parts[-1].strip()
                break
        results.append(make_job(source, raw_title, company, LOCATION,
            extract_salary(snippet), "See listing", link.split("?")[0], snippet))
    return results

def scrape_seek_google():
    results = []
    print("  📡 SEEK (via Google)...")
    for title in ["QA Automation Engineer","Test Automation Engineer","SDET",
                  "Senior Test Automation Engineer","QA Engineer","Automation Tester",
                  "Performance Test Engineer","Test Lead"]:
        results.extend(google_search_jobs("seek.com.au", title))
        time.sleep(2)
    results = deduplicate(results)
    print(f"     → {len(results)} SEEK roles")
    return results

def scrape_indeed_google():
    results = []
    print("  📡 Indeed (via Google)...")
    for title in ["QA Automation Engineer","Test Automation Engineer","SDET","Senior Test Automation Engineer"]:
        results.extend(google_search_jobs("au.indeed.com", title))
        time.sleep(2)
    results = deduplicate(results)
    print(f"     → {len(results)} Indeed roles")
    return results

def scrape_linkedin_google():
    results = []
    print("  📡 LinkedIn (via Google)...")
    extra = "insurance OR defence OR rail OR aerospace OR embedded OR workforce"
    for title in ["QA Automation Engineer","Test Automation Engineer","SDET","Senior Test Engineer"]:
        results.extend(google_search_jobs("linkedin.com/jobs", title, extra))
        time.sleep(2)
    results = deduplicate(results)
    print(f"     → {len(results)} LinkedIn roles")
    return results

# Curated known companies — always included
CURATED = [
    {"source":"Company","title":"QA Automation Engineer (Insurance)","company":"Insurance Client via Agency",
     "location":"Sydney CBD — Hybrid","salary":"~$700–$800/day + Super (≈$140k–$165k p.a.)","type":"Contract 12mo",
     "link":"https://www.seek.com.au/automation-testing-jobs/in-All-Sydney-NSW",
     "snippet":"Playwright specialist. Senior contract. Actively listed on SEEK.","_sector":"Insurance"},
    {"source":"Company","title":"Test Lead / QA Engineer","company":"Teachers Health",
     "location":"Sydney NSW — Hybrid","salary":"Competitive + health subsidy","type":"Permanent",
     "link":"https://www.teachershealth.com.au/about-us/careers",
     "snippet":"Health insurance not-for-profit. Lead digital testing projects.","_sector":"Insurance"},
    {"source":"Company","title":"QA Engineer","company":"Humanforce",
     "location":"Sydney NSW (Remote possible)","salary":"Not listed","type":"Permanent",
     "link":"https://www.humanforce.com/about/careers",
     "snippet":"Workforce Management SaaS ~200–500 staff.","_sector":"Workforce Management"},
    {"source":"Wabtec Careers","title":"Senior Software Engineer (Embedded Rail)","company":"Wabtec Australia",
     "location":"Rydalmere Sydney NSW — Onsite","salary":"Competitive + Medibank health","type":"Permanent",
     "link":"https://wabtec.wd1.myworkdayjobs.com/en-US/wabtec_careers",
     "snippet":"Safety-critical embedded rail systems. Strong sector match.","_sector":"Rail"},
    {"source":"DroneShield Careers","title":"Senior QA Automation Engineer","company":"DroneShield",
     "location":"Sydney CBD — Onsite","salary":"Not listed (Senior, competitive)","type":"Permanent",
     "link":"https://www.droneshield.com/careers",
     "snippet":"Counter-drone defence AI. ~320 staff ASX-listed. CI/CD, Go, Jira. STRONG MATCH.","_sector":"Defence"},
    {"source":"Company","title":"Software Quality Engineer","company":"Fivecast",
     "location":"Sydney NSW","salary":"Not listed","type":"Permanent",
     "link":"https://www.fivecast.com/careers",
     "snippet":"Defence intelligence/OSINT software ~100–200 staff.","_sector":"Defence"},
    {"source":"Company","title":"QA / Test Engineer","company":"QinetiQ Australia",
     "location":"Sydney NSW","salary":"Not listed","type":"Permanent",
     "link":"https://www.qinetiq.com/en-au/careers",
     "snippet":"Defence testing & evaluation ~200–500 AU staff.","_sector":"Defence"},
    {"source":"Company","title":"QA / Test Engineer (UAV Systems)","company":"Anduril Industries AU",
     "location":"Sydney NSW","salary":"Not listed (US-backed, competitive)","type":"Permanent",
     "link":"https://www.anduril.com/careers",
     "snippet":"Defence autonomous/UAV systems. Growing AU team.","_sector":"Air"},
    {"source":"Company","title":"SDET Lead","company":"Neara (Infrastructure Tech)",
     "location":"Sydney NSW — Hybrid","salary":"Not listed + equity","type":"Permanent",
     "link":"https://www.neara.com/careers",
     "snippet":"Models power grids. Playwright/Cypress/Selenium/Python. STRONG MATCH.","_sector":"Embedded Systems"},
]

def scrape_all():
    print("\n" + "─"*50)
    all_raw = []
    all_raw.extend(scrape_remotive());  time.sleep(1)
    all_raw.extend(scrape_jobicy());    time.sleep(1)
    all_raw.extend(scrape_arbeitnow()); time.sleep(1)
    all_raw.extend(scrape_seek_google())
    all_raw.extend(scrape_indeed_google())
    all_raw.extend(scrape_linkedin_google())

    qa_jobs = [j for j in all_raw if is_qa_role(j["title"], j.get("snippet",""))]
    print(f"\n  Filtered: {len(qa_jobs)} QA roles from {len(all_raw)} total")

    sector_jobs = {s: [] for s in SECTORS}
    for job in qa_jobs:
        s = classify_sector(job["title"], job["company"], job.get("snippet",""))
        if s and s in sector_jobs:
            sector_jobs[s].append(job)

    for c in CURATED:
        s = c.get("_sector","Insurance")
        if s in sector_jobs:
            sector_jobs[s].append(c)

    for s in sector_jobs:
        sector_jobs[s] = deduplicate(sector_jobs[s])
        print(f"  {s}: {len(sector_jobs[s])} listings")

    return sector_jobs

# ─────────────────────────────────────────────
# EXCEL BUILDER
# ─────────────────────────────────────────────

COL_HEADERS = ["Source","Job Title","Company","Location","Salary","Type","Date Found","Application Link","Notes"]
COL_WIDTHS  = [13,40,30,28,26,18,13,55,38]

def thin(color="DDDDDD"):
    s = Side(style="thin", color=color)
    return Border(left=s, right=s, top=s, bottom=s)

def hdr(cell, hex_color):
    cell.font = Font(bold=True, color="FFFFFF", name="Arial", size=10)
    cell.fill = PatternFill("solid", start_color=hex_color)
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = thin("FFFFFF")

def dat(cell, ri, bold=False, color="000000", italic=False):
    cell.fill = PatternFill("solid", start_color="EFF3FB" if ri%2==0 else "FFFFFF")
    cell.font = Font(name="Arial", size=9, bold=bold, color=color, italic=italic)
    cell.alignment = Alignment(vertical="center", wrap_text=True)
    cell.border = thin()

def add_summary_sheet(wb, sector_jobs):
    ws = wb.create_sheet("Summary", 0)
    ws.sheet_view.showGridLines = False
    ws.merge_cells("A1:E1")
    c = ws["A1"]; c.value = "QA / Test Automation - Sydney Job Tracker"
    c.font = Font(bold=True, name="Arial", size=16, color="FFFFFF")
    c.fill = PatternFill("solid", start_color="1A237E")
    c.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 44
    ws.merge_cells("A2:E2")
    c = ws["A2"]; c.value = f"Generated: {TODAY_STR}  |  Target: ${SALARY_MIN:,}-${SALARY_MAX:,}  |  Remote/Hybrid/Onsite  |  Sydney NSW"
    c.font = Font(italic=True, name="Arial", size=10, color="444444")
    c.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[2].height = 22
    ws.row_dimensions[3].height = 8
    for i,(h,w) in enumerate(zip(["Sector","Listings","Priority","Status","Sheet"],[28,16,14,18,24]),1):
        c = ws.cell(row=4, column=i, value=h); hdr(c,"1A237E")
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[4].height = 28
    priorities = {"Insurance":"High","Workforce Management":"Medium","Rail":"Medium",
                  "Defence":"High","Air":"Medium","Embedded Systems":"High"}
    total = 0
    for r,(sector,jobs) in enumerate(sector_jobs.items(),5):
        count = len(jobs); total += count; clr = SECTOR_COLORS[sector]
        for ci,val in enumerate([sector,count,priorities[sector],"Active",sector[:31]],1):
            c = ws.cell(row=r,column=ci,value=val)
            c.fill = PatternFill("solid", start_color="F0F4FF" if r%2==0 else "FFFFFF")
            c.font = Font(name="Arial", size=10, bold=(ci==1), color=clr if ci==1 else "000000")
            c.alignment = Alignment(horizontal="left" if ci==1 else "center", vertical="center")
            c.border = thin()
        ws.row_dimensions[r].height = 24
    tr = 5+len(sector_jobs)
    for ci,val in enumerate(["TOTAL",total,"","",""],1):
        c = ws.cell(row=tr,column=ci,value=val)
        c.font = Font(bold=True,name="Arial",size=11)
        c.fill = PatternFill("solid",start_color="C5CAE9")
        c.alignment = Alignment(horizontal="center" if ci!=1 else "left",vertical="center")
        c.border = thin()
    ws.row_dimensions[tr].height = 28
    ql = tr+2
    ws.merge_cells(f"A{ql}:E{ql}")
    c = ws[f"A{ql}"]; c.value = "Quick Job Board Links"
    c.font = Font(bold=True,name="Arial",size=10,color="FFFFFF")
    c.fill = PatternFill("solid",start_color="283593")
    c.alignment = Alignment(horizontal="center",vertical="center")
    ws.row_dimensions[ql].height = 24
    links = [
        ("SEEK - QA Engineer Sydney","https://www.seek.com.au/qa-engineer-jobs/in-All-Sydney-NSW"),
        ("SEEK - Automation Testing","https://www.seek.com.au/automation-testing-jobs/in-All-Sydney-NSW"),
        ("Indeed - QA Engineer Sydney","https://au.indeed.com/QA-Engineer-jobs-in-Sydney-NSW"),
        ("LinkedIn - QA Automation AU","https://au.linkedin.com/jobs/qa-automation-engineer-jobs"),
        ("Glassdoor - QA Sydney","https://www.glassdoor.com.au/Job/sydney-qa-engineer-jobs-SRCH_IL.0,6_IC2235932_KO7,18.htm"),
        ("Remotive - Remote QA Jobs","https://remotive.com/remote-jobs/qa"),
        ("DroneShield Careers","https://www.droneshield.com/careers"),
        ("Neara Careers","https://www.neara.com/careers"),
        ("Wabtec AU Careers","https://wabtec.wd1.myworkdayjobs.com/en-US/wabtec_careers"),
        ("Humanforce Careers","https://www.humanforce.com/about/careers"),
        ("Fivecast Careers","https://www.fivecast.com/careers"),
    ]
    for i,(label,url) in enumerate(links,ql+1):
        ws.merge_cells(f"A{i}:E{i}")
        c = ws[f"A{i}"]; c.value = f"  {label}  ->  {url}"; c.hyperlink = url
        c.font = Font(name="Arial",size=9,color="1A237E",underline="single")
        c.alignment = Alignment(horizontal="left",vertical="center",indent=2)
        c.fill = PatternFill("solid",start_color="EFF3FB" if i%2==0 else "FFFFFF")
        c.border = thin(); ws.row_dimensions[i].height = 20
    ws.freeze_panes = "A5"

def add_sector_sheet(wb, sector, jobs):
    clr = SECTOR_COLORS[sector]
    ws = wb.create_sheet(title=sector[:31])
    ws.sheet_properties.tabColor = clr
    ws.sheet_view.showGridLines = False
    ws.merge_cells("A1:I1")
    c = ws["A1"]; c.value = f"{sector}  |  QA / Test Automation  |  Sydney NSW  |  {TODAY_STR}"
    c.font = Font(bold=True,name="Arial",size=12,color="FFFFFF")
    c.fill = PatternFill("solid",start_color=clr)
    c.alignment = Alignment(horizontal="center",vertical="center")
    ws.row_dimensions[1].height = 32
    ws.merge_cells("A2:I2")
    c = ws["A2"]; c.value = f"Target: ${SALARY_MIN:,}-${SALARY_MAX:,}  |  {len(jobs)} listings  |  Remote / Hybrid / Onsite"
    c.font = Font(italic=True,name="Arial",size=9,color="555555")
    c.alignment = Alignment(horizontal="center",vertical="center")
    ws.row_dimensions[2].height = 18
    ws.row_dimensions[3].height = 30
    for ci,(h,w) in enumerate(zip(COL_HEADERS,COL_WIDTHS),1):
        c = ws.cell(row=3,column=ci,value=h); hdr(c,clr)
        ws.column_dimensions[get_column_letter(ci)].width = w
    if not jobs:
        ws.merge_cells("A4:I4")
        c = ws["A4"]; c.value = "No listings found today. Check Summary sheet for quick links."
        c.font = Font(italic=True,name="Arial",size=9,color="888888")
        c.alignment = Alignment(horizontal="center",vertical="center")
        ws.row_dimensions[4].height = 22
    else:
        for ri,job in enumerate(jobs,4):
            ws.row_dimensions[ri].height = 50
            row_vals = [job.get("source",""),job.get("title",""),job.get("company",""),
                        job.get("location",""),job.get("salary","Not listed"),job.get("type","Not listed"),
                        TODAY_STR,job.get("link",""),job.get("snippet","")[:180]]
            for ci,val in enumerate(row_vals,1):
                c = ws.cell(row=ri,column=ci,value=val)
                dat(c,ri,bold=(ci==2),color=clr if ci==1 else "000000",italic=(ci==9))
                if ci==8 and str(val).startswith("http"):
                    c.hyperlink = val
                    c.font = Font(name="Arial",size=9,color="1565C0",underline="single")
    ws.freeze_panes = "A4"
    if jobs:
        ws.auto_filter.ref = f"A3:I{3+len(jobs)}"

def build_excel(sector_jobs, filepath):
    wb = Workbook(); wb.remove(wb.active)
    add_summary_sheet(wb, sector_jobs)
    for sector,jobs in sector_jobs.items():
        add_sector_sheet(wb, sector, jobs)
    wb.save(filepath)
    print(f"\nExcel saved: {filepath}")

# ─────────────────────────────────────────────
# EMAIL
# ─────────────────────────────────────────────

def send_email(filepath, total_count):
    if SENDER_PASSWORD == "roldrybcqvqizzsz":
        print("\n" + "="*55)
        print("  EMAIL NOT SENT — App Password not configured")
        print("="*55)
        print("  1. Go to: https://myaccount.google.com/apppasswords")
        print("  2. Sign in as: karunakarhv@gmail.com")
        print("  3. App name: QA Job Tracker  -> click Create")
        print("  4. Copy the 16-character password")
        print("  5. Open job_scraper.py")
        print("  6. Replace YOUR_APP_PASSWORD with it (no spaces)")
        print("  7. Run again -> email will work immediately")
        print("="*55)
        return

    today = datetime.date.today().strftime("%d %B %Y")
    subject = f"QA Job Report - Sydney NSW - {today} ({total_count} listings)"
    body = f"""Hi Karun,

Your daily QA / Test Automation job report for Sydney, NSW is attached.

Date:      {today}
Location:  Sydney NSW (Remote / Hybrid / Onsite)
Target:    ${SALARY_MIN:,} - ${SALARY_MAX:,}
Listings:  {total_count} found across all sectors

Sectors: Insurance | Workforce Management | Rail | Defence | Air | Embedded Systems
Sources: SEEK | Indeed | LinkedIn | Remotive | Jobicy | Arbeitnow + Curated leads

Open the Excel file - each coloured tab = one industry sector with direct Apply links.

--
QA Job Tracker | Auto-runs daily at 7:00 AM AEST
"""
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL; msg["To"] = RECIPIENT_EMAIL; msg["Subject"] = subject
    msg.attach(MIMEText(body,"plain"))
    with open(filepath,"rb") as f:
        part = MIMEBase("application","octet-stream"); part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f'attachment; filename="{os.path.basename(filepath)}"')
    msg.attach(part)
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        print(f"Email sent to {RECIPIENT_EMAIL}")
    except smtplib.SMTPAuthenticationError:
        print("\nEMAIL FAILED - Wrong App Password")
        print("  Go to: https://myaccount.google.com/apppasswords")
        print("  Generate a NEW App Password for karunakarhv@gmail.com")
        print("  Paste it into SENDER_PASSWORD in this script (no spaces)")
    except Exception as e:
        print(f"Email error: {e}")

# ─────────────────────────────────────────────
# ENTRYPOINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("="*55)
    print("  QA Job Tracker - Sydney NSW")
    print(f"  {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*55)
    sector_jobs = scrape_all()
    total = sum(len(v) for v in sector_jobs.values())
    print(f"\nTotal listings: {total}")
    out_dir  = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(out_dir, f"QA_Jobs_Sydney_{DATE_TAG}.xlsx")
    build_excel(sector_jobs, filepath)
    send_email(filepath, total)