"""
Flags can be passed into regular expression functions as parameters, to change the behaviour of the pattern.
"""
import re


""" re.I / re.IGNORECASE
CASE-INSENSITIVE matching
"""
output = re.search("Python", "python is awesome", flags=re.I)
print(output)


output = re.search("AWESOME", "python is awesome", flags=re.IGNORECASE)
print(output)

