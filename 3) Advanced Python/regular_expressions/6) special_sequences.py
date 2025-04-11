"""
Special Sequences are predefined character classes or shorthand notations that simplify pattern writing.
They begin with a backslash followed by a character and are used to match specific types of characters
 or positions in the text.

Note: COMBINING SPECIAL SEQUENCES WITH QUANTIFIES ALLOW YOU TO PERFORM REALLY POWERFUL PATTERN MATCHING.
"""
import re

text_to_search = "His Index No: 007"

# Match all the digits (0-9)
print(re.search(r'\d', text_to_search))  # Match only first 0
print(re.search(r'\d+', text_to_search))  # With quantifiers. Match 007


# Match all the Non-Digits
print(re.search(r'\D', text_to_search))
print(re.search(r'\D+', text_to_search))


# Match all the Alphanumeric characters
print(re.search(r'\w', text_to_search))


# Match all the Non-Alphanumeric characters
print(re.search(r'\W+', text_to_search))


# Match all the whitespaces
print(re.search(r'\s', text_to_search))


# Match all the non-whitespaces
print(re.search(r'\S', text_to_search))
