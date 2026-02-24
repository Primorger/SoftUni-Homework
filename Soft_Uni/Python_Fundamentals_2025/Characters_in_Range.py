# ord() chr()
character_1 = input()
character_2 = input()

for index in range(ord(character_1) + 1, ord(character_2)):
    print(chr(index), end=" ")