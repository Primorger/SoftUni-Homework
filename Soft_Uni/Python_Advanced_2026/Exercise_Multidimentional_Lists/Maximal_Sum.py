rows, cols = [int(part) for part in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_submatrix = None

for i in range(rows-2):
    for j in range(cols-2):
        current_submatrix = [[matrix[row][col] for col in range(j, j+3)] for row in range(i, i+3)]

        if max_submatrix is None:
            max_submatrix = current_submatrix

        if sum(sum(row) for row in max_submatrix) < sum(sum(row) for row in current_submatrix):
            max_submatrix = current_submatrix

print(f"Sum = {sum(sum(row) for row in max_submatrix)}")
[print(' '.join(map(str, row))) for row in max_submatrix]
