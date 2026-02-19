# Give this a quick shot: Extract the float -23.5 from this string and check if it's between -24.0 and -22.0. 
# "Analysis Complete: True | Peak: -1.2dBFS | Integrated_Loudness: -23.5 LKFS | Channel_Count: 6"

import re
def extract_and_check_loudness(log_line):
    # Use regex to find the float value before "LKFS"
    match = re.search(r'(-?\d+\.\d+)\s*LKFS', log_line)
    if match:
        loudness_value = float(match.group(1))
        print(f"Extracted Loudness: {loudness_value} LKFS")
        # Check if it's between -24.0 and -22.0
        if -24.0 < loudness_value < -22.0:
            print("Loudness is within the acceptable range.")
        else:
            print("Loudness is outside the acceptable range.")
    else:
        print("Loudness value not found in the log line.")

# Test the function with the provided log line
log_line = "Analysis Complete: True | Peak: -1.2dBFS | Integrated_Loudness: -23.5 LKFS | Channel_Count: 6"
extract_and_check_loudness(log_line)
