command = ""

while command != "End":
    command = input()

    output = ""

    if command == "End":
        break
    elif command == "SoftUni":
        pass
    else:
        for char in command:
            for _ in range(2):
                output += char
    
        print(output)