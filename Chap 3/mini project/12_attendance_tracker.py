# Attendance Tracker

attendance = {}

while True:
    print("\n1. Mark Attendance")
    print("2. View Attendance")
    print("3. Attendance Percentage")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        status = input("Enter P for Present or A for Absent: ").upper()

        if status in ["P", "A"]:
            attendance.setdefault(name, []).append(status)
            print("Attendance marked")
        else:
            print("Invalid status")

    elif choice == "2":
        for name, records in attendance.items():
            print(name, ":", records)

    elif choice == "3":
        name = input("Enter student name: ")

        if name in attendance:
            records = attendance[name]
            present = records.count("P")
            total = len(records)

            percentage = (present / total) * 100

            print("Attendance Percentage:", percentage, "%")
        else:
            print("Student not found")

    elif choice == "4":
        break

    else:
        print("Invalid choice")