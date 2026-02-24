n = int(input())

matrix = []

for _ in range(n):
    data = list(input())
    matrix.append(data)

def search_symbol(char = str):
    row, col = None, None
    for i in range(n):
        for j in range(n):
            if char == matrix[i][j]:
                row, col = i, j
                return f"({row}, {col})"
    return f"{char} does not occur in the matrix"

needed_symbol = input()

print(search_symbol(needed_symbol))