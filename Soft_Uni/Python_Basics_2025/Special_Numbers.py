number = int(input())

for num in range(1_111, 10_000):
    num_str = str(num)
    is_special = True
    for digit in num_str:
        digit = int(digit)
        if digit == 0 or number % digit != 0:
            is_special = False
            break

    if is_special:
        print(num, end=" ")

