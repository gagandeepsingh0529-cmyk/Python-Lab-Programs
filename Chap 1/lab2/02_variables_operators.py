# Variables, Operators, Input and Output

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Modulus:", a % b)
else:
    print("Division by zero is not allowed")

print("Power:", a ** b)
print("Is a greater than b?", a > b)