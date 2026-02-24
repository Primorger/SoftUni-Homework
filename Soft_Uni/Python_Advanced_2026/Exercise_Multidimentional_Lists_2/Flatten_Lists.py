strings = input().split("|")

matrix = []

for i in range(len(strings) -1, -1, -1):
    current_string = strings[i].strip()
    if current_string:
        matrix.append(current_string)

for row in matrix:
    elements = row.split()
    for element in elements:
        print(element, end=" ")
        