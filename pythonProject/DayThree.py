file_path = "C:/Users/BT_4N2_18/PycharmProjects/pythonProject/input.txt"
with open(file_path, "r") as f:
    content = f.read()

num = ["1","2","3","4","5","6","7","8","9","0"]



valid = ['m', 'u', 'l', '(', num, ',', num, ')']

sum = 0
index = 0
for i in range(len(content)):
    if content[i] == "m":
        if content[i + 1] == "u":
            if content[i + 2] == "l":
                if content[i + 3] == "(":
                    num1 = ""
                    for j in range(3):
                        b = j + 5
                        if content[b] in num:
                            num1 + content[b]
                    if content[i + 4 + len(num1)] == ",":
                        num2 = ""
                        for j in range(3):
                            c = j + 5 + len(num1)
                            if content[c] in num:
                                num2 + content[c]
                        if content[i + 5 + len(num1) + len(num2)] == ")":
                            sum += int(num1) + int(num2)

print(sum)
    # maybe mr das was right but I aint backin down

