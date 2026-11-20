# Student Data Manager Using Files

filename = "students.txt"

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        age = input("Enter age: ")

        with open(filename, "a") as file:
            file.write(name + "," + roll + "," + age + "\n")

        print("Student details saved successfully")

    elif choice == "2":
        try:
            with open(filename, "r") as file:
                print("\nStudent Records:")

                for line in file:
                    print(line.strip())

        except FileNotFoundError:
            print("No student records found")

    elif choice == "3":
        break

    else:
        print("Invalid choice")