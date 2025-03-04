# Integer Operations in Python

a = 10
b = 3

# 1. Basic Arithmetic Operations
# Addition (+), Subtraction (-), Multiplication (*), Division (/)

print("Addition:", a + b)  # 10 + 3 = 13
print("Subtraction:", a - b)  # 10 - 3 = 7
print("Multiplication:", a * b)  # 10 * 3 = 30
print("Division (float result):", a / b)  # 10 / 3 = 3.3333


# 2. Floor Division (//)
# This returns the quotient without the remainder.
print("Floor Division:", a // b)  # 10 // 3 = 3


# 3. Modulus (%)
# Returns the remainder of the division.
print("Modulus:", a % b)  # 10 % 3 = 1


# 4. Exponentiation (**)
# Raises a number to the power of another number.
print("Exponentiation:", a ** b)  # 10^3 = 1000


# 5. Absolute Value (abs)
# Returns the absolute (positive) value of an integer.
c = -15
print("Absolute Value:", abs(c))  # abs(-15) = 15


# 6. Built-in Functions: min() and max()
# Finds the minimum and maximum values among given numbers.

print("Minimum:", min(a, b, c))  # min(10, 3, -15) = -15
print("Maximum:", max(a, b, c))  # max(10, 3, -15) = 10


# 7. Converting Integers
# Converting float/strings to integers using int()
d = "25"
e = 3.99
print("String to Integer:", int(d))  # "25" -> 25
print("Float to Integer (truncates decimal part):", int(e))  # 3.99 -> 3

