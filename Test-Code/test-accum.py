# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
    listItems = list(s)
    strAccum = ''
    for idx in range(0, len(listItems)):
        strAccum += listItems[idx].upper()
        strAccum += listItems[idx].lower() * idx + '-'
    return strAccum[:-1]

print(accum("ZpglnRxqenU"))
