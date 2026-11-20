# Student Grading System

name = input("Enter student name: ")

m1 = float(input("Enter marks in subject 1: "))
m2 = float(input("Enter marks in subject 2: "))
m3 = float(input("Enter marks in subject 3: "))

total = m1 + m2 + m3
average = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    grade = "A"

elif average >= 80:
    grade = "B"

elif average >= 70:
    grade = "C"

elif average >= 60:
    grade = "D"

elif average >= 40:
    grade = "E"

else:
    grade = "F"

print("Grade:", grade)