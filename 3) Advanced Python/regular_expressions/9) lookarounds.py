"""
Lookarounds are a set of zero-width assertions in regex that allow you to match something based on,
what comes before or after it, without including that part in the actual match.

There are 4 types
    1)  Positive Lookahead
    2)  Negative Lookahead
    1)  Positive Lookbehind
    1)  Negative Lookbehind
"""
import re

""" 1) Positive Lookahead
SYNTAX: (?=...)
"""
output = re.findall(r'\w+(?=\d)', 'apple2 banana3 mango')  # Match any word followed by a digit
# print(output)


""" 2) Negative Lookahead
SYNTAX: (?!...)
"""
output = re.findall(r'\w+(?!\d)', 'apple2 banana mango3')   # Match any word not followed by a digit:
# print(output)


""" 3) Positive Lookbehind
SYNTAX: (?<=...)
"""
output = re.findall(r'(?<=\$)\d+', 'Price: $1200')  # Match digits only if preceded by $:
# print(output)


""" 4) Negative Lookbehind 
SYNTAX: (?<!...)
"""
output = re.findall(r'(?<!USD)\d+', 'USD1200 EUR1300')  # Match digits not preceded by USD:
print(output)
