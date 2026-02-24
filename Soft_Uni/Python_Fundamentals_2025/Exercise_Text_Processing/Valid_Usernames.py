usernames = input().split(", ")

for username in usernames:
    username_is_valid = True
    if not (3 <= len(username) <= 16):
        username_is_valid = False
    for char in username:
        if not (char.isalnum() or char == "-" or char == "_"):
            username_is_valid = False
            break
    if " " in username:
        username_is_valid = False
    if username_is_valid:
        print(username)
