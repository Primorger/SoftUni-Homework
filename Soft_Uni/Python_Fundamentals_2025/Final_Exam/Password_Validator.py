password = input()

while True:
    command = input()
    if command == "Complete":
        break

    parts = command.split()

    if parts[0] == "Make":
        if parts[1] == "Upper":
            index = int(parts[2])
            password = password[:index] + password[index].upper() + password[index + 1:]
            print(password)
        if parts[1] == "Lower":
            index = int(parts[2])
            password = password[:index] + password[index].lower() + password[index + 1:]
            print(password)

    elif parts[0] == "Insert":
        if len(parts) < 3:
            continue
        try:
            index = int(parts[1])
            character = parts[2]
        except:
            continue
        
        if not (0 <= index <= len(password)):
            continue
        password = password[:index] + character + password[index:]
        print(password)

    elif parts[0] == "Replace":
            if len(parts) < 3:
                continue
            try:
                value = int(parts[2])
                character = parts[1]
            except:
                continue
            if len(character) != 1:
                continue
            if character in password:
                new_character = chr(ord(character) + value)
                password = password.replace(character, new_character)
                print(password)

    elif parts[0] == "Validation":
        if len(password) < 8:
            print("Password must be at least 8 characters long!")

        if not all(char.isalnum() or char == '_' for char in password):
            print("Password must consist only of letters, digits and _!")

        if not any(char.isupper() for char in password):
            print("Password must consist at least one uppercase letter!")

        if not any(char.islower() for char in password):
            print("Password must consist at least one lowercase letter!")

        if not any(char.isdigit() for char in password):
            print("Password must consist at least one digit!")    
