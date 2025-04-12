"""
Groups can be used for partitioning the regex match.
We can take the pieces of the output one by one
"""
import re

text_to_search = "abc123def"

pattern = re.compile(r'(abc)(123)')

""" 1)   re.findall()
All the groups will be stored as tuples inside a list
"""
print(pattern.findall(text_to_search))


""" 2)   re.finditer()
Groups can be accesses separately.
"""
for match in pattern.finditer(text_to_search):
    print(match.group(0))   # Special group. A combination of all the groups
    print(match.group(1))  # First Group (abc)
    print(match.group(2))  # Second Group (123)


""" 3)   Non-Capturing Groups
A non-capturing group in regex is a group used for grouping parts of a pattern without saving (or "capturing")
 the matched text for backreferencing.
 
Meaning that, you won't be able to access the group with group number like in the previous example.
"""
text = "catdogcat123"
matches = re.search(r"(?:cat|dog)(123)", text)
print(matches.group(1))
# print(matches.group(2))  # Error: No such group


""" 4)   Named Capturing Groups
A named capturing group allows you to give a name to a group instead of using numbers like .group(1), .group(2), etc.

SYNTAX: (?P<name>pattern)
"""
text = "Name: Alice, Age: 25"
pattern = r"Name: (?P<username>\w+), Age: (?P<age>\d+)"
match = re.search(pattern, text)

print(match.group('username'))
print(match.group('age'))
