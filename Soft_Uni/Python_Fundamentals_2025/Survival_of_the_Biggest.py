integers_as_str = input().split()
count_to_remove = int(input())
integers = []

for char in integers_as_str:
    integers.append(int(char))

for _ in range(count_to_remove):
    integers.remove(min(integers))

print(', '.join(map(str, integers)))