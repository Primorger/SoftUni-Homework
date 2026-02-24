special_chars = "-,.?!"

with open("Exercise_File_Handling\\Even_Lines\\text.txt") as file:
    
    for i, line in enumerate(file):
        if i % 2 == 0:
            for char in special_chars:
                line = line.replace(char, "@")

            print(" ".join(reversed(line.split())))