n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

def find_diagonal(diagonal: bool, size: int):
    diagonal_components = []

    if diagonal:
        for y in range(size):
            diagonal_components.append(matrix[y][y])
    else:
        for y in range(size):
            diagonal_components.append(matrix[y][size - 1 - y])

    return diagonal_components

primary_diagonal_sum = sum(find_diagonal(True, n))
secondary_diagonal_sum = sum(find_diagonal(False, n))

difference = abs(primary_diagonal_sum - secondary_diagonal_sum)

print(difference)
