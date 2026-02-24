def reverse(lst):
    lst1 = []
    for i in range(len(lst) - 1, 0, -1):
        lst1.append(lst[i])
    print(lst1)
reverse([1, 2, 3])