"""
Groups can be used for partitioning the regex match.
We can take the pieces of the output one by one
"""
import re

text_to_search = "abc123def"

pattern = re.compile(r'(abc)(123)')

# with re.findall(), all the groups will be stored as tuples inside a list
print(pattern.findall(text_to_search))

# With re.finditer(), groups can be accesses separately.
for match in pattern.finditer(text_to_search):
    print(match.group(0))   # Special group. A combination of all the groups
    print(match.group(1))  # First Group (abc)
    print(match.group(2))  # Second Group (123)
