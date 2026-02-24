bottom_range = input()
top_range = input()

for num1 in range(int(bottom_range[0]), int(top_range[0]) + 1):
    for num2 in range(int(bottom_range[1]), int(top_range[1]) + 1):
        for num3 in range(int(bottom_range[2]), int(top_range[2]) + 1):
            for num4 in range(int(bottom_range[3]), int(top_range[3]) + 1):
                if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0 and num4 % 2 != 0:
                    print(f"{num1}{num2}{num3}{num4}", end=" ")