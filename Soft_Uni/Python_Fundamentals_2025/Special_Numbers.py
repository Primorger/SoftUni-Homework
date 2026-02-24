n = int(input())

for i in range(1, n + 1):
    i_str = str(i)
    sum = 0
    for num in i_str:
        sum += int(num)
    
    print(f"{i} -> {sum in (5, 7, 11)}")