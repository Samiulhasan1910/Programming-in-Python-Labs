# Lab 03: Variables, Data Types, Operators, and Branching Statements

# Problem 1: Swap the values of two variables
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("Before swap: a =", a, "b =", b)
temp = a
a = b
b = temp
print("After swap: a =", a, "b =", b)


# Problem 2: Distance between two points
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Distance =", d)


# Problem 3: Even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")


# Problem 4: Vowel or not vowel
ch = input("Enter a character: ")
if ch in "aeiouAEIOU":
    print(ch, "is a vowel")
else:
    print(ch, "is not a vowel")


# Problem 5: Marks to grade (AIUB grading)
marks = float(input("Enter marks (0-100): "))
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A+")
elif marks >= 85:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B+")
elif marks >= 75:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C+")
elif marks >= 65:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D+")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")
