n = int(input())

matrix = [[int(part) for part in input().split()] for _ in range(n)]

while True:
    command = input().split()
    if command[0] == "END":
        break

    operation, row, col, value = command

    if int(row) >= n or int(col) >= n or int(row) < 0 or int(col) < 0:
        print("Invalid coordinates")
        continue

    if operation == "Add":
        matrix[int(row)][int(col)] += int(value)
    elif operation == "Subtract":
        matrix[int(row)][int(col)] -= int(value)

[print(*r) for r in matrix]