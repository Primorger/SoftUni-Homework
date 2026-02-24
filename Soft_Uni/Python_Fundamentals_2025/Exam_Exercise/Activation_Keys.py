activation_key = input()
while True:
    command = input()
    if command == "Generate":
        break
    command = command.split(">>>")
    if command[0] == "Contains":
        if command[1] in activation_key:
            print(f"{activation_key} contains {command[1]}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        start = int(command[2])
        end = int(command[3])
        segment = activation_key[start:end]
        if command[1] == "Upper":
            segment = segment.upper()
        else:
            segment = segment.lower()
        activation_key = activation_key[:start] + segment + activation_key[end:]
        print(activation_key)
    elif command[0] == "Slice":
        start = int(command[1])
        end = int(command[2])
        activation_key = activation_key[:start] + activation_key[end:]
        print(activation_key)
print(f"Your activation key is: {activation_key}")