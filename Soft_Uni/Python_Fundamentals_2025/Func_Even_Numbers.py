numbers = input().split()
number = []

def convert_user_input(string):
    for char in string:
        number.append(int(char))

def is_even(num):
    if num % 2 == 0:
        return True
    return False

convert_user_input(numbers)
even_numbers = list(filter(is_even, number))
print(even_numbers)