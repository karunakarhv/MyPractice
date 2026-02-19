import re

def get_flagged_sessions(log_lines):
    flagged_ids = []
    
    for line in log_lines:
        # 1. Clean and split by the pipe character
        parts = [p.strip() for p in line.split('|')]
        
        # 2. Extract ID (Removing "ID:" prefix)
        session_id = parts[0].split('ID:')[-1].strip()
        
        # 3. Check for Buffer_Underrun
        # We look through all parts to see if the error exists
        has_underrun = any("Buffer_Underrun" in p for p in parts)
        
        # 4. Extract and Compare Latency
        # We find the part containing 'LATENCY', extract digits, and convert to int
        latency_val = 0
        for p in parts:
            if "LATENCY:" in p:
                # Use regex to grab only the numbers (e.g., '450' from '450ms')
                match = re.search(r'\d+', p)
                if match:
                    latency_val = int(match.group())
        
        # 5. Logic: Flag if either condition is met
        if has_underrun or latency_val > 200:
            flagged_ids.append(session_id)
            
    return flagged_ids

# Testing with the data provided
logs = [
    "[2026-02-07 10:15:01] ID:9922 | STATUS:OK | LATENCY:120ms | CODEC:AC4",
    "[2026-02-07 10:15:05] ID:9923 | STATUS:FAIL | ERR:Buffer_Underrun | LATENCY:450ms",
    "[2026-02-07 10:15:10] ID:9924 | STATUS:OK | LATENCY:110ms | CODEC:AC4",
    "[2026-02-07 10:15:15] ID:9925 | STATUS:OK | LATENCY:210ms | CODEC:EAC3"
]

print(f"Flagged IDs: {get_flagged_sessions(logs)}") 
# Expected Output: ['9923', '9925']