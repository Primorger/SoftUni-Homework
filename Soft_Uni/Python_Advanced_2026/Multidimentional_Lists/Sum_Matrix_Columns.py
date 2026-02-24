n_rows, n_cols = map(int, input().split(", "))

matrix = []

for _ in range(n_rows):
    row = list(map(int, input().split()))
    matrix.append(row)

column_sums = []

for i in range(n_cols):
    print(sum(matrix[j][i] for j in range(n_rows)))