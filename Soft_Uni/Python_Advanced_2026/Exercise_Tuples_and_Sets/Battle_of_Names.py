n = int(input())
odd_set = set()
even_set = set()

for row in range(1, n + 1):
    name = input()
    ascii_sum = sum(ord(char) for char in name)
    result = ascii_sum // row
    
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    output = list(odd_set.union(even_set))
elif odd_sum > even_sum:
    output = list(odd_set.difference(even_set))
else:
    output = list(odd_set.symmetric_difference(even_set))

print(", ".join(map(str, output)))
