command = input()

lst = command.split(" ")
lst_1 = []

for char in lst:
    lst_1.append(int(char) * -1)
print(lst_1)