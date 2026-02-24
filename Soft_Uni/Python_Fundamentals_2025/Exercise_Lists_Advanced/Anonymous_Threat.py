files = input().split()

def merge_files(start_index, end_index):
    global files
    start_index = max(0, start_index)
    end_index = min(len(files) - 1, end_index)
    
    if start_index < end_index:
        merged = ''.join(files[start_index:end_index + 1])
        files[start_index:end_index + 1] = [merged]

def divide_files(index, partitions):
    global files
    if index >= len(files):
        return
    
    string = files[index]
    if partitions <= 0:
        return
    
    part_length = len(string) // partitions
    result = []
    
    for i in range(partitions - 1):
        result.append(string[i * part_length:(i + 1) * part_length])
    
    result.append(string[(partitions - 1) * part_length:])
    
    files[index:index + 1] = result

while True:
    list_of_data = input().split()
    if list_of_data[0] == "3:1":
        break
    command, a, b = list_of_data[0], int(list_of_data[1]), int(list_of_data[2])

    if command == "merge":
        merge_files(a, b)
    elif command == "divide":
        divide_files(a, b)

print(' '.join(files))