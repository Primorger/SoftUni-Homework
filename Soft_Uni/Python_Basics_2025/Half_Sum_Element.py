n = int(input())

max_num = 0
tot_sum = 0

for _ in range(n):
    current_number = int(input())
    if current_number > max_num:
        max_num = current_number
    tot_sum += current_number
tot_sum -= max_num

if tot_sum == max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    diff = abs(max_num - tot_sum)
    print("No")
    print(f"Diff = {diff}")