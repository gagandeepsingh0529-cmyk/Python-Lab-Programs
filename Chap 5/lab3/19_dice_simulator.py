# Dice Simulator Using Random Module

import random

while True:
    choice = input(
        "Press Enter to roll dice or Q to quit: "
    )

    if choice.lower() == "q":
        print("Thank you for playing!")
        break

    dice = random.randint(1, 6)

    print("You rolled:", dice)