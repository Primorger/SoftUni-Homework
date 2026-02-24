n_rows, n_cols = map(int, input().split(", "))

matrix = []
total_sum = 0

for _ in range(n_rows):
    row = list(map(int, input().split(", ")))
    matrix.append(row)
    total_sum += sum(row)

print(total_sum)
print(matrix)