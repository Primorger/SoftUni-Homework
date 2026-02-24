rows, cols = [int(part) for part in input().split()]

matrix = []
data = []

for row in range(rows):
    for col in range(cols):
        data.append(f"{chr(row+97)}{chr((col+row)+97)}{chr(row+97)}")
    matrix.append(data)
    data = []

[print(' '.join(row)) for row in matrix]

# rows, cols = map(int, input().split())
# [print(' '.join(f"{chr(row+97)}{chr((col+row)+97)}{chr(row+97)}" for col in range(cols))) for row in range(rows)]