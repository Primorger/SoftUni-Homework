file_path = input()

for index in range(len(file_path) - 1, -1, -1):
    if file_path[index] == "\\":
        file_name = file_path[index + 1:]
        break

for index in range(len(file_name) - 1, -1, -1):
    if file_name[index] == ".":
        name = file_name[:index]
        extension = file_name[index + 1:]
        break

print(f"File name: {name}")
print(f"File extension: {extension}")
