import os

while True:
    command = input()
    if command == "End":
        break

    command, filename, *args = command.split("-")

    if command == "Create":
        open("Exercise_File_Handling\\File_Manipulator\\" + filename, "w",).close()

    elif command == "Add":
        with open("Exercise_File_Handling\\File_Manipulator\\" + filename, "a") as file:
            file.write(f"{args[0]}\n")

    elif command == "Replace":
        try:
            with open("Exercise_File_Handling\\File_Manipulator\\" + filename, "r+") as file:
                content = file.read()
                file.seek(0)
                file.truncate(0)
                file.write(content.replace(args[0], args[1]))
        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        if os.path.exists("Exercise_File_Handling\\File_Manipulator\\" + filename):
            os.remove()
        else:
            print("An error occurred")