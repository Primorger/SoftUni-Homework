command = input().split(" | ")
dictionary = {}

for item in command:
    word, definition = item.split(": ")

    if word not in dictionary:
        dictionary[word] = []

    dictionary[word].append(definition)

words_to_check = input().split(" | ")

teacher_command = input()

if teacher_command == "Test":
    for word in words_to_check:
        if word in dictionary:
            print(f"{word}:")

            for definition in dictionary[word]:
                print(f" -{definition}")
                
elif teacher_command == "Hand Over":
    print(" ".join(dictionary.keys()))