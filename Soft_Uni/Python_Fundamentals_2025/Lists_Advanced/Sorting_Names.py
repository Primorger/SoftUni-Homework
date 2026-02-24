command = input().split(", ")

sorted_names = sorted(command, key= lambda x: (-len(x), x))

print(sorted_names)