numbers = input().split()
numbers_int = []

def convert_user_input(string):
    for char in string:
        numbers_int.append(int(char))

convert_user_input(numbers)

print(f"The minimum number is {min(numbers_int)}")
print(f"The maximum number is {max(numbers_int)}")
print(f"The sum number is: {sum(numbers_int)}")