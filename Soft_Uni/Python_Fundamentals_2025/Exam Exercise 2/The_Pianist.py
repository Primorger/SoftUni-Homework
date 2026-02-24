def add_piece(collection, piece, composer, key):
    if piece in collection:
        print(f"{piece} is already in the collection!")
    else:
        collection[piece] = {"composer": composer, "key": key}
        print(f"{piece} by {composer} in {key} added to the collection!")

def remove_piece(collection, piece):
    if piece in collection:
        del collection[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")

def change_key(collection, piece, new_key):
    if piece in collection:
        collection[piece]["key"] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def main_function():
    n = int(input())
    collection = {}

    for _ in range(n):
        piece, composer, key = input().split("|")
        collection[piece] = {"composer": composer, "key": key}
    
    while True:
        command = input()

        if command == "Stop":
            break

        command_parts = command.split("|")
        action = command_parts[0]

        if action == "Add":
            add_piece(collection, command_parts[1], command_parts[2], command_parts[3])
        elif action == "Remove":
            remove_piece(collection, command_parts[1])
        elif action == "ChangeKey":
            change_key(collection, command_parts[1], command_parts[2])

    for piece, info in collection.items():
        print(f'{piece} -> Composer: {info["composer"]}, Key: {info["key"]}')

main_function()