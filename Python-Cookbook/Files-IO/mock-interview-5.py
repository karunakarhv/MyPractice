# Practice Regular Expressions for Log File Analysis

# Task: Write a regex pattern to extract the following fields from a log line:
# - Timestamp (e.g., "2026-02-07 10:15:01")
# - Session ID (e.g., "9922")
# - Status (e.g., "OK")
# - Latency (e.g., "120ms")
# - Codec (e.g., "AC4")
import re
def extract_log_fields(log_line):
    pattern = r'\[(.*?)\] ID:(\d+) \| STATUS:(\w+) \| LATENCY:(\d+ms) \| CODEC:(\w+)'
    match = re.search(pattern, log_line)
    if match:
        timestamp = match.group(1)
        session_id = match.group(2)
        status = match.group(3)
        latency = match.group(4)
        codec = match.group(5)
        return {
            'timestamp': timestamp,
            'session_id': session_id,
            'status': status,
            'latency': latency,
            'codec': codec
        }
    else:
        return None

# Test the function with a sample log line
log_line = "[2026-02-07 10:15:01] ID:9922 | STATUS:OK | LATENCY:120ms | CODEC:AC4"
fields = extract_log_fields(log_line)
print(fields)
# Expected Output:
# {'timestamp': '2026-02-07 10:15:01', 'session_id': '9922', 'status': 'OK', 'latency': '120ms', 'codec': 'AC4'}

# Practice Regular Expressions for Error Detection
# Task: Write a regex pattern to detect if a log line contains the error "Buffer_Underrun" and extract the session ID if it does.
def detect_buffer_underrun(log_line):
    pattern = r'ID:(\d+) \|.*Buffer_Underrun'
    match = re.search(pattern, log_line)
    if match:
        session_id = match.group(1)
        return session_id
    else:
        return None
# Test the function with a sample log line
log_line = "[2026-02-07 10:15:05] ID:9923 | STATUS:FAIL | ERR:Buffer_Underrun | LATENCY:450ms"
session_id = detect_buffer_underrun(log_line)
print(session_id)
# Expected Output: '9923'