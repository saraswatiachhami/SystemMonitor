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
3. Open a text editor or IDE (e.g., VS Code, PyCharm, or Notepad) and create a python file(e.g: SystemMonitor.py) and write the Python code in SystemMonitor.py .
4. Create a sample log file named system_logs.txt in the same directory/folder and add some log entries to the file.
5. Open a Terminal or Command Prompt in the same directory.
6. Run the code in the terminal by: python SystemMonitor.py
7. Observe the Output: If the log file contains any of the suspicious patterns, the script will print alerts to the console.

## Assumptions or limitations in my implementation
  # Assumptions
  1. Log File Format
  2. Pattern Matching
  3. Timestamp
  4. Real-Time Monitoring
  5. Single Log File

  # Limitations
  1. No Advanced Pattern Matching
  2. No Log Rotation Support
  3. No Error Handling
  4. Performance Issues with Large Log Files
  5. No Configuration File
