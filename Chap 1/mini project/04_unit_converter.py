# Unit Converter

while True:
    print("\nUNIT CONVERTER")
    print("1. Kilometres to Miles")
    print("2. Miles to Kilometres")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilograms to Pounds")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "6":
        break

    value = float(input("Enter value: "))

    if choice == "1":
        print("Miles:", value * 0.621371)

    elif choice == "2":
        print("Kilometres:", value / 0.621371)

    elif choice == "3":
        print("Fahrenheit:", (value * 9/5) + 32)

    elif choice == "4":
        print("Celsius:", (value - 32) * 5/9)

    elif choice == "5":
        print("Pounds:", value * 2.20462)

    else:
        print("Invalid choice")