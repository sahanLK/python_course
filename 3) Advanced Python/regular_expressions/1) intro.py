"""
Regular expressions with literal characters.
Exploring all the main functions provided by re module, to work with regexes.
"""
import re


""" 1) re.match()
Matches a pattern at the beginning of the string. Match only 1 occurrence.
"""
match = re.match(pattern='Python', string='Python is Fun')
# print(match)


""" 2) re.search()
Searches for a pattern anywhere in the string. Match only 1 occurrence.
"""
match = re.search(pattern='Fun', string='Python is Fun Fun')
# print(match)


""" 3) re.findall()
Returns a list of all non-overlapping matches in the string.
"""
matches = re.findall(pattern='Python', string='Python is Fun and Python is Easy')
# print(match)


""" 4) re.finditer()
Returns an iterator yielding match objects for all non-overlapping matches in the string.
"""
matches = re.finditer(pattern='Python', string='Python is Fun and Python is Easy')
# for item in matches:
#     print(item)


""" 5) re.sub()
Substitutes all occurrences of a pattern with a specified replacement string.
"""
output = re.sub(pattern='Python', repl="Java", string='Python is Fun and Python is Easy')
# print(output)


""" 5) re.split()
Splits the string at all occurrences of the pattern.
"""
output = re.split(pattern=r'\s', string='Python is Fun')
# print(output)


""" 5) re.compile()
This can be used to compile a pattern once and reuse that over and over again.
Output will be a re object that can access all the above methods.
"""
pattern = re.compile("Hello")

# Using the pattern
# for item in pattern.findall('Hello World'):
#     print(item)

# Using the same pattern again with another string
output = pattern.search("Hello Python")
# print(output)