# CSV-Based Payroll Management System

import csv
import os

filename = "payroll.csv"

# Create CSV file with headings
if not os.path.exists(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Basic Salary",
                         "Allowance", "Deduction", "Net Salary"])

while True:
    print("\n1. Add Employee")
    print("2. View Payroll")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")

        basic = float(input("Enter basic salary: "))
        allowance = float(input("Enter allowance: "))
        deduction = float(input("Enter deduction: "))

        net_salary = basic + allowance - deduction

        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                emp_id,
                name,
                basic,
                allowance,
                deduction,
                net_salary
            ])

        print("Employee payroll saved successfully")
        print("Net Salary:", net_salary)

    elif choice == "2":
        with open(filename, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                print(row)

    elif choice == "3":
        break

    else:
        print("Invalid choice")