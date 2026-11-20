# Log File Reader Program

filename = "sample.log"

try:
    with open(filename, "r") as file:
        lines = file.readlines()

    print("Log File Contents:\n")

    for line in lines:
        print(line.strip())

    errors = 0

    for line in lines:
        if "ERROR" in line.upper():
            errors += 1

    print("\nTotal Lines:", len(lines))
    print("Total Errors:", errors)

except FileNotFoundError:
    print("Log file not found")