import re

text = "Product: Laptop, Price: $1200"
pattern = r"Product: (?P<item>\w+), Price: \$(?P<price>\d+)"

match = re.search(pattern, text)
print(f"Item: {match.group("item")} -> Price: {match.group('price')}")



