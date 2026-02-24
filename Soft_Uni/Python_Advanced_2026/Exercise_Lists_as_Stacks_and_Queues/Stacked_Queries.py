N = int(input())

queries = []

for _ in range(N):
    command = input().split()
    code = command[0]

    if code == "1":
        number = command[1]
        queries.append(number)
    elif code == "2":
        if len(queries) == 0:
            continue
        queries.pop()
    elif code == "3":
        if len(queries) > 0:
            print(max(int(num) for num in queries))
    elif code == "4":
        if len(queries) > 0:
            print(min(int(num) for num in queries))

queries.reverse()
print(", ".join(queries))