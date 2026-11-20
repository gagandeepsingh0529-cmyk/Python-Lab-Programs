# JSON-Based Log File Analyzer

import json
import os

filename = "logs.json"

# Create sample log file if it does not exist
if not os.path.exists(filename):
    logs = [
        {"level": "INFO", "message": "Application started"},
        {"level": "ERROR", "message": "Database error"},
        {"level": "WARNING", "message": "Low memory"},
        {"level": "ERROR", "message": "File not found"},
        {"level": "INFO", "message": "Application running"}
    ]

    with open(filename, "w") as file:
        json.dump(logs, file, indent=4)

# Read JSON file
with open(filename, "r") as file:
    logs = json.load(file)

info = 0
warning = 0
error = 0

for log in logs:
    level = log["level"].upper()

    if level == "INFO":
        info += 1

    elif level == "WARNING":
        warning += 1

    elif level == "ERROR":
        error += 1

print("LOG ANALYSIS REPORT")
print("-------------------")

print("Total Logs:", len(logs))
print("INFO:", info)
print("WARNING:", warning)
print("ERROR:", error)

print("\nError Messages:")

for log in logs:
    if log["level"].upper() == "ERROR":
        print(log["message"])