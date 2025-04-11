import re


# Beginning of a string
re.match(r"^Hello", "Hello world")
re.match(r"^world", "Hello world")   # No Match


# End of a string
re.search(r"world$", "Hello world")
re.search(r"Hello$", "Hello world")  # No Match


# Word Boundary
output = re.search(r"\bcat\b", "a cat sat")
output = re.search(r"\bcat\b", "concatenate")  # No Match

# Not a word boundary
output = re.search(r"\Bcat\B", "concatenate")

output = re.search(r"\Bcat\B", "a cat sat")  # No Match
print(output)
