n = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

def find_diagonal(diagonal: str, size: int):
    diagonal_components = []

    if diagonal == "Primary":
        for y in range(size):
            diagonal_components.append(matrix[y][y])
    elif diagonal == "Secondary":
        for y in range(size):
            diagonal_components.append(matrix[y][size - 1 - y])

    diagonal_components_str = [str(part) for part in diagonal_components]
    
    print(f'{diagonal} diagonal: {", ".join(diagonal_components_str)}. Sum: {sum(diagonal_components)}')

find_diagonal("Primary", n)
find_diagonal("Secondary", n)