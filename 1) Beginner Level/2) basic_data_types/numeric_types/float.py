# Float Operations in Python

a = 10.5
b = 3.2


# 1. Basic Arithmetic Operations
# Addition (+), Subtraction (-), Multiplication (*), Division (/)
print("Addition:", a + b)  # 10.5 + 3.2 = 13.7
print("Subtraction:", a - b)  # 10.5 - 3.2 = 7.3
print("Multiplication:", a * b)  # 10.5 * 3.2 = 33.6
print("Division:", a / b)  # 10.5 / 3.2 = 3.28125


# 2. Floor Division (//)
# Returns the largest integer value <= the division result.
print("Floor Division:", a // b)  # 10.5 // 3.2 = 3.0


# 3. Modulus (%)
# Returns the remainder of the division.
print("Modulus:", a % b)  # 10.5 % 3.2 = 0.8999999999999995 (floating-point precision issue)


# 4. Exponentiation (**)
# Raises a number to the power of another number.
print("Exponentiation:", a ** b)  # 10.5^3.2 = 13838.219


# 5. Absolute Value (abs)
# Returns the absolute (positive) value of a float.
c = -15.75
print("Absolute Value:", abs(c))  # abs(-15.75) = 15.75


# 6. Built-in Functions: min() and max()
# Finds the minimum and maximum values among given floats.
print("Minimum:", min(a, b, c))  # min(10.5, 3.2, -15.75) = -15.75
print("Maximum:", max(a, b, c))  # max(10.5, 3.2, -15.75) = 10.5


# 7. Rounding Floats
# Rounding to the nearest integer or specified decimal places.
print("Rounded (nearest integer):", round(a))  # round(10.5) = 10
print("Rounded (2 decimal places):", round(a / b, 2))  # round(3.28125, 2) = 3.28


# 8. Converting Floats
# Converting integers/strings to floats using float()
d = "25.75"
e = 3
print("String to Float:", float(d))  # "25.75" -> 25.75
print("Integer to Float:", float(e))  # 3 -> 3.0


# 9. Formatting Floats
# Using f-strings or format() to control decimal places.
print(f"Formatted float: {a:.2f}")  # 10.50
print("Formatted float:", format(a, ".2f"))  # 10.50
