
# def calculate(num1, num2):
#     if num1 > num2:
#         for i in range(num1):
#             print(i * 2)
#
#     if num2 > num1:
#         for i in range(num2):
#             print(i + 2)
#
# calculate(2, 3)

def change_str(name):
    condition = True

    while condition:
        for char in name: # n, a, m, e
            for i in range(2): # 0, 1
                print(char * 2)

                if char == 'm':
                    condition = False
                    break


change_str("name")

# nn
# nn
# aa
# aa
# mm
# ee
# ee




