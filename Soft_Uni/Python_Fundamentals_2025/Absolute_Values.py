command = input().split()

def absolute_values(lmnt):
    return abs(float(lmnt))

lst_abs = list(map(absolute_values, command))

print(lst_abs)