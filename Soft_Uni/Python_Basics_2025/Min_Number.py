num = input()
min_num = int(num)

while num != "Stop":
    if int(num) < min_num:
        min_num = int(num)
    num = input()
else:
    print(min_num)