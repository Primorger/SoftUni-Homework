n = int(input())

matrix = []

for _ in range(n):
    data = [int(part) for part in input().split()]
    matrix.append(data)

sum = 0

for i in range(n):
    value = matrix[i][i]
    sum += value

print(sum)