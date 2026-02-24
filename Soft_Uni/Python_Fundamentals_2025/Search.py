n = int(input())

special_str = input()

lst = []
special_lst = []

for _ in range(n):
    obj = input()
    lst.append(obj)
    if special_str in obj:
        special_lst.append(obj)
print(lst)
print(special_lst)