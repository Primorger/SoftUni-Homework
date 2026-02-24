rows, cols = [int(part) for part in input().split(", ")]

matrix = []
max_submatrix = [0, 0, 0, 0]
current_submatrix = [0, 0, 0, 0]

for _ in range(rows):
    data = [int(part) for part in input().split(", ")]
    matrix.append(data)

for i in range(rows-1):
    for j in range(cols-1):
        try:
            current_submatrix = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
        except:
            pass

        if sum(max_submatrix) < sum(current_submatrix):
            max_submatrix[0] = current_submatrix

print(f"{max_submatrix[0]} {max_submatrix[1]}\n{max_submatrix[2]} {max_submatrix[3]}")
print(sum(max_submatrix))
