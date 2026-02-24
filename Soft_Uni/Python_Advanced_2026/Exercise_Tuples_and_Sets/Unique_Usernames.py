n = int(input())

usernames = []

for _ in range(n):
    usernames.append(input())

usernames = set(usernames)

for username in usernames:
    print(username)