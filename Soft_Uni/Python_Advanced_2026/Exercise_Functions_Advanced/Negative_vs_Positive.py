def sum_nums(*nums):
    negative_sum = 0
    positive_sum = 0

    for num in nums:
        if num > 0:
            positive_sum += num
        else:
            negative_sum += num
    return negative_sum, positive_sum
    
numbers = [int(x) for x in input().split()]
n_sum, p_sum = sum_nums(*numbers)

print(n_sum)
print(p_sum)

if abs(n_sum) > p_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")