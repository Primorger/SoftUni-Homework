N = int(input())
names = []

for _ in range(N):
    names.append(input())

unique_names = set(names)

for name in unique_names:
    print(name)
