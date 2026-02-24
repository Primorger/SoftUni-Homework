notes = [0] * 10
while True:
    command = input()
    if command == "End":
        break
    tokens = command.split("-")
    importance = int(tokens[0])
    task = tokens[1]
    notes[importance - 1] = task

result = [task for task in notes if task != 0]
print(result)