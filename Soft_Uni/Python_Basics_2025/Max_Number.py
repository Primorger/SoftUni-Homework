num = input()
max_num = int(num)

while num != "Stop":
    if int(num) > max_num:
        max_num = int(num)
    num = input()
else:
    print(max_num)