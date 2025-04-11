import re

""""
Character-Set only match one character. But there are different ways to specify the characters
"""

text_to_match = """
character-Set only match one char

123456785
"""

# Specifying a single character to match
pattern = re.compile(r"[0-9]")

# Specifying a range of characters to match (numbers from 0 to 5)
pattern = re.compile(r"[0-5]")

# Specifying a range of characters to match (All simple letters)
pattern = re.compile(r"[a-z]")

# Specifying a range of characters to match (All Capital letters)
pattern = re.compile(r"[A-Z]")

# Specifying a range of characters to match (All Simple and Capital letters)
pattern = re.compile(r"[A-Z a-z]")

# Caret inside the Character-set matches, all the characters that are NOT inside the Character-set
pattern = re.compile(r"[^A-Z a-z]")

for match in pattern.finditer(text_to_match):
    print(match)
