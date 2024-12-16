file_path = "C:/Users/BT_4N2_18/PycharmProjects/pythonProject/input.txt"
with open(file_path, "r") as f:
    content = f.read()

num = ["1","2","3","4","5","6","7","8","9","0"]





sum = 0
index = 0
for i in range(len(content)):
    index += 1
    if content[i] == "m":
        if content[i + 1] == "u":
            if content[i + 2] == "l":
                if content[i + 3] == "(":
                    num1 = ""
                    for j in range(3):
                        b = j + 4 + i
                        if content[b] in num:
                            num1 += content[b]
                        else:
                            break
                    if content[i + 4 + len(num1)] == ",":
                        num2 = ""
                        for j in range(3):
                            c = j + 5 + len(num1) + i
                            if content[c] in num:
                                num2 += content[c]
                            else:
                                break
                        if content[i + 5 + len(num1) + len(num2) ] == ")":
                            sum += int(num1) * int(num2)

print(sum)
# print(index)
    # maybe mr das was right but I aint backin down, imma make this work!

# for i in range(len(content)):
#     if content[i] == "m":
#         if content[i + 1] == "u":
#             if content[i + 2] == "l":
#                 if content[i + 3] == "(":
#                     num1 = ""
#                     for j in range(3):
#                         b = j + 3
#                         if content[b] in num:
#                             num1 += content[b]
#                             # print(content[b])
#                     print(num1)
#
# print(sum)



# sum = 0
# index = 0
# for i in range(len(content)):
#     if content[i] == "m":
#         if content[i + 1] == "u":
#             if content[i + 2] == "l":
#                 if content[i + 3] == "(":
#                     num1 = ""
#                     for j in range(3):
#                         b = j + 3
#                         if content[b] in num:
#                             num1 += content[b]
#                     if content[i + 4 + len(num1)] == ",":
#                         num2 = ""
#                         for j in range(3):
#                             c = j + 5 + len(num1)
#                             if content[c] in num:
#                                 num2 += content[c]
#                         if content[i + 5 + len(num1) + len(num2)] == ")":
#                             sum += int(num1) * int(num2)
#
# print(sum)\


