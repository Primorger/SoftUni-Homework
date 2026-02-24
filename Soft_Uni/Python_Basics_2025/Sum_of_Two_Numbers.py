lower_bound = int(input())
higher_bound = int(input())
num = int(input())
combination_counter = 0
broken = False
for x in range(lower_bound, higher_bound + 1):
    for y in range(lower_bound, higher_bound + 1):
        combination_counter += 1
        if x + y == num:
            print(f"Combination N:{combination_counter} ({x} + {y} = {num})")
            broken = True
            break
    if broken:
        break
else:
    print(f"{combination_counter} combinations - neither equals {num}")