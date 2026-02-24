n = int(input())

matrix = []
bunny = None

for r in range(n):
    row = input().split()
    matrix.append(row)
    for c in range(n):
        if row[c] == "B":
            bunny = (r, c)

directions = {
    "up":    (-1, 0),
    "down":  (1, 0),
    "left":  (0, -1),
    "right": (0, 1)
}

best_dir = ""
best_sum = float("-inf")
best_path = []

for direction, (dr, dc) in directions.items():
    r, c = bunny
    curr_sum = 0
    path = []

    while True:
        r += dr
        c += dc

        if r < 0 or r >= n or c < 0 or c >= n:
            break
        if matrix[r][c] == "X":
            break

        curr_sum += int(matrix[r][c])
        path.append([r, c])

    if path and curr_sum > best_sum:
        best_sum = curr_sum
        best_dir = direction
        best_path = path

print(best_dir)
for p in best_path:
    print(p)
print(best_sum)
