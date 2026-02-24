lower_bound = int(input())
upper_bound = int(input())

for num in range(lower_bound, upper_bound + 1):
    num_str = str(num)
    even_sum = 0
    odd_sum = 0
    for i in range(len(num_str)):
        digit = int(num_str[i])
        if i % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    if even_sum == odd_sum:
        print(num, end=" ")