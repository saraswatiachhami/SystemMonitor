import re
from datetime import datetime

def monitor_log_file(log_file_path):
    # Define the suspicious patterns to look for
    suspicious_patterns = [
        "failed login",
        "unauthorized access",
        "malicious activity detected"
    ]
    
    # Compile regular expressions for each pattern
    pattern_regex = [re.compile(pattern, re.IGNORECASE) for pattern in suspicious_patterns]
    
    # Open the log file and read it line by line
    with open(log_file_path, 'r') as file:
        for line in file:
            # Check each line against the suspicious patterns
            for regex in pattern_regex:
                if regex.search(line):
                    # If a pattern is found, generate an alert
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    alert_message = f"ALERT: {regex.pattern.upper()} DETECTED AT {timestamp}"
                    print(alert_message)
                    # Optionally, you can log this message to a file or another system
                    # log_alert(alert_message)
                    break  # Stop checking other patterns once a match is found

# Example usage
log_file_path = 'system_logs.txt'  # Replace with your actual log file path
monitor_log_file(log_file_path)