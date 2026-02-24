numbers = input().split()
numbers_int = []

def convert_user_input(string):
    for char in string:
        numbers_int.append(int(char))

convert_user_input(numbers)

print(sorted(numbers_int))