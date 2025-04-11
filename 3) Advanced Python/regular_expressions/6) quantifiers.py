import re

# 0 or more
output = re.findall(r"ab*", "ab abb abbb a")

# 1 or more
output = re.findall(r"ab+", "ab abb abbb a")

# 0 or one (Optional)
output = re.findall(r"ab?", "ab abb abbb a")

# Exact n times
output = re.findall(r"ab{2}", "ab abb abbb a")

# At Least n times
output = re.findall(r"\d{2,}", "1 12 123 1234")

# Between n and m times
output = re.findall(r"\d{2,3}", "1 12 123 1234")

# *?, +?, {n,m}? — Non-Greedy / Lazy Quantifiers
"""
GREEDY QUANTIFIER
* is a greedy quantifier, meaning it tries to match as much text as possible.

NON-GREEDY (LAZY) QUANTIFIER
*? is a non-greedy, meaning it matches the minimum amount of text possible to satisfy the pattern 
(Nothing more, nothing less)
"""
output = re.findall(r"<.*?>", "<br>bold</br><i>italic</i>")

print(output)
