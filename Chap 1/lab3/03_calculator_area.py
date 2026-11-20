# Calculator and Area Calculation

import math

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Area of Circle")
    print("6. Area of Rectangle")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "7":
        break

    elif choice in ["1", "2", "3", "4"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", a + b)
        elif choice == "2":
            print("Result:", a - b)
        elif choice == "3":
            print("Result:", a * b)
        elif choice == "4":
            if b != 0:
                print("Result:", a / b)
            else:
                print("Cannot divide by zero")

    elif choice == "5":
        r = float(input("Enter radius: "))
        print("Area of Circle:", math.pi * r * r)

    elif choice == "6":
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        print("Area of Rectangle:", l * b)

    else:
        print("Invalid choice")