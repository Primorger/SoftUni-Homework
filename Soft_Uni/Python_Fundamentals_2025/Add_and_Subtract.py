num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

def sum_numbers(num_1, num_2):
    return num_1 + num_2

def subtract(sum_of_numbers, num_3):
    return sum_of_numbers - num_3

print(subtract(sum_numbers(num_1, num_2), num_3))