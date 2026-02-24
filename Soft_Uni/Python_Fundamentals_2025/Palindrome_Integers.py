numbers = input().split(", ")
answer = []

def backwards(string):
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return reversed_string

def is_palindrome(number):
    return number == backwards(number)

for chr in numbers:
    if is_palindrome(chr):
        print("True")
    else:
        print("False")
