
file = open('temp.txt', 'w+')

# Reading a file
content = file.read()
print(content)

# Writing to a file
file.write('ABC')

file.close()

# with open('temp.txt', 'w+') as file:
#     content = file.read()
#     file.write('some')


# pattern = re.compile('You can')
#
# for match in pattern.finditer(content):
#     print(match)

