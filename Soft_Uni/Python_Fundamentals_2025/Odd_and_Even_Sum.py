command = input()
numbers = []

def convert_user_input(string):
    for char in string:
        numbers.append(int(char))

def is_even(num):
    if num % 2 == 0:
        return True
    return False

convert_user_input(command)

even_numbers = filter(is_even, numbers)
odd_numbers = filter(lambda x: not is_even(x), numbers)

print(f"Odd sum = {sum(odd_numbers)}, Even sum = {sum(even_numbers)}")