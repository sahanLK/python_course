
# Strings can be defined inside single or double quotes

name = 'Hello World'

# Access items by index
# print(name[2])
# print(name[-2]) # Accessing items by negative index



# String Methods

# print(dir(name))
# print(name.lower())
# print(name.split('H'))
# print(name.capitalize())
# print(name.upper())
# print(name.index('S'))
# print(name.swapcase())
# print(name.endswith('World'))
# print(name.startswith('Hell'))
# print(name.startswith())


# String Formatting

# Method 1: With Fstrings
# name = "Sahan"
# desc = f"My name is {name}"

age = 25
# Method 2: Using format method
# desc = "My name is {1}. My age is {0}".format(name, age)


# String Slicing

desc = "Hello world"
result = desc[::-1]

print(result)
