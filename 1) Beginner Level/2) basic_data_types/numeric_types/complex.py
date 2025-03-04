# Complex Number Operations in Python

a = 3 + 4j
b = 1 - 2j


# 1. Defining Complex Numbers
# A complex number has a real part and an imaginary part, written as 'a + bj'.
print("Complex Number a:", a)
print("Complex Number b:", b)


# 2. Basic Arithmetic Operations
# Addition, Subtraction, Multiplication, Division
print("Addition:", a + b)  # (3+4j) + (1-2j) = (4+2j)
print("Subtraction:", a - b)  # (3+4j) - (1-2j) = (2+6j)
print("Multiplication:", a * b)  # (3+4j) * (1-2j) = (11+2j)
print("Division:", a / b)  # (3+4j) / (1-2j) = (-1+2j)


# 3. Conjugate of a Complex Number
print("Conjugate of a:", a.conjugate())  # (3+4j) -> (3-4j)


# 4. Real and Imaginary Parts
print("Real part of a:", a.real)  # 3.0
print("Imaginary part of a:", a.imag)  # 4.0
