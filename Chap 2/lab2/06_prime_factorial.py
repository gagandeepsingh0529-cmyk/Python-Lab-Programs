# Prime Number and Factorial

n = int(input("Enter a number: "))

# Factorial
factorial = 1

if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    for i in range(1, n + 1):
        factorial = factorial * i

    print("Factorial:", factorial)

# Prime Number
if n < 2:
    print("Not a Prime Number")
else:
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")