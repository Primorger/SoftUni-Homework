string = input()
vowels = ('a', 'o', 'u', 'e', 'i')

for char in string:
    if not char.lower() in vowels:
        print(char, end="")