# SystemMonitor

## Description of Project(SystemMonitor - Basic Log Parsing and Alerting System)
The SystemMonitor project is designed to automate the process of monitoring system logs for security-related events or errors. It reads a log file (e.g., from a SIEM or other security tools), scans each log entry for predefined suspicious patterns (such as "failed login", "unauthorized access", or "malicious activity detected"), and generates alerts when such patterns are detected.

## Features
1. Log Parsing
2. Pattern Matching
3. Alerting
4. Customizable Patterns

## Usecase
This tool is particularly useful for security teams or system administrators who need to monitor large volumes of logs for potential threats or system errors. It can be integrated into a larger security monitoring pipeline or used as a standalone tool for quick log analysis.

## Steps to run the code
1. Ensure that Python is installed on your system. You can download it from the official website: python.org.
2. Create a folder for your project, e.g: Techincal Assessment and navigate to the folder.
3. Open a text editor or IDE (e.g., VS Code, PyCharm, or Notepad) and create a python file(e.g: SystemMonitor.py) in that folder and write the Python code in SystemMonitor.py .
4. Create a sample log file named system_logs.txt in the same directory/folder and add some log entries to the file.
5. Open a Terminal or Command Prompt in the same directory.
6. Run the code in the terminal by: python SystemMonitor.py
7. Observe the Output: If the log file contains any of the suspicious patterns, the script will print alerts to the console.

## Assumptions or limitations in my implementation
  # Assumptions
  1. Log File Format:
     -The log file is assumed to be a plain text file with one log entry per line and The script does not handle structured log formats like JSON, XML, or CSV.
  2. Pattern Matching:
     -The suspicious patterns are hardcoded and case-insensitive and It assumes that the patterns (e.g., "failed login") are sufficient to detect security issues.
  3. Timestamp:
     -The script uses the current system time (datetime.now()) for alert timestamps, not the timestamp from the log entry itself. This assumes that the log entries do not contain timestamps or that the 
      current time is sufficient for alerting.
  5. Real-Time Monitoring:
     -The script reads the log file once and does not monitor it in real-time. It assumes that the log file is static during execution.
  7. Single Log File:
     -The script processes a single log file at a time. It does not handle multiple log files or directories.

  # Limitations
  1. No Advanced Pattern Matching:
     -The script uses simple string matching with regular expressions. It cannot detect complex or context-dependent patterns (e.g., multiple failed logins from the same IP address within a short time frame).
  2. No Log Rotation Support:
     -The script does not handle log rotation, where log files are archived or deleted after reaching a certain size or age.
  3. No Error Handling:
     -The script does not handle errors such as:
        Missing or inaccessible log files.
        Permission issues when reading the log file.
        Corrupted or improperly formatted log entries.
  4. Performance Issues with Large Log Files:
     -The script reads the entire log file line by line, which may be inefficient for very large log files. It does not use buffering or parallel processing.
  5. No Configuration File:
     -The script does not use a configuration file to define patterns, log file paths, or alerting rules. All settings are hardcoded.
