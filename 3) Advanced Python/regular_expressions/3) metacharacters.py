"""
Metacharacters
"""
import re

text_to_search = "My lucky number is 1290"

""" 1) .
Matches any character except a new line
"""
output = re.findall(r'.', text_to_search)
# print(output)

# for match in re.finditer(r'.', text_to_search):
#     print(match)


""" 2) ^
Matches the start of a string.
"""
# print(re.search(r'^My', text_to_search))  # Match
# print(re.findall(r'^lucky', text_to_search))    # No match (Empty list)


""" 3) $
Matches the end of a string.
"""
# print(re.search(r'1290$', text_to_search))  # Match
# print(re.findall(r'lucky$', text_to_search))    # No match (Empty list)


""" 4) []
Matches any character inside the brackets
"""
chars = "1234 abcd"
output = re.findall(r'[ab12]', chars)
# print(output)


""" 5) |
OR operator, matches the pattern on the left or the pattern on the right.
"""
output = re.search(r'ab|12', chars)
# print(output)


""" 6) \
Can be used for escaping any special character
"""
# Dot in below pattern doesn't have that superpower of matching everything. It's just literal dot.
# Same can be done for escaping other characters also.
pattern = re.compile(r'\.')
output = pattern.search('Hello.')
print(output)
