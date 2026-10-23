# Lab 04: Loops

# Problem 1: for loop over a sequence
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


# Problem 2: Countdown using a while loop
n = int(input("Enter a number: "))
while n >= 0:
    print(n)
    n = n - 1


# Problem 3: Exponentiation of a number
base = int(input("Enter base: "))
power = int(input("Enter power: "))
result = 1
for i in range(power):
    result = result * base
print(base, "to the power", power, "=", result)


# Problem 4: Sum of all primes below 1000
total = 0
for num in range(2, 1000):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        total = total + num
print("Sum of primes below 1000 =", total)


# Problem 5: Fibonacci numbers below N
N = int(input("Enter N: "))
a = 0
b = 1
while a < N:
    print(a)
    c = a + b
    a = b
    b = c
