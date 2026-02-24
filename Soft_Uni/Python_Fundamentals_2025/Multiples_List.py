multiple = int(input())
n = int(input())
lst = []

for i in range(multiple, n * multiple + 1, multiple):
    lst.append(i)
print(lst)