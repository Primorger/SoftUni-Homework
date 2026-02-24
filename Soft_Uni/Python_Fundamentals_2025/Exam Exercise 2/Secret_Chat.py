message = input()

while True:
    command = input()
    if command == "Reveal":
        break
    
    command = command.split(":|:")

    if command[0] == "InsertSpace":
        message = list(message)
        message.insert(int(command[1]), " ")
        message = "".join(message)

    elif command[0] == "Reverse":
        if command[1] in message:
            message = message.replace(command[1], "", 1)
            message += command[1][::-1]
        else:
            print("error")
            continue

    elif command[0] == "ChangeAll":
        message = message.replace(command[1], command[2])
    
    print(message)

print(f"You have a new text message: {message}")