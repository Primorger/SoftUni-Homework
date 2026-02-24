height = int(input())

for i in range(1, height + 1):
    for l in range(0, i):
        print("*", end="")
    print()
for i in range(height - 1, 0, -1):
    for l in range(0, i):
        print("*", end="")
    print()