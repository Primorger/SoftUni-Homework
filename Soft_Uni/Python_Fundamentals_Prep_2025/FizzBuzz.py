print("Welcome to FizzBuzz!")

num = int(input())

def get_input(num):
    
    if num % 3 == 0 and num % 7 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 7 == 0:
        return "Buzz"
    elif "3" in str(num):
        return "Almost Fizz"
    else:
        return num

for i in range(1, num + 1):
    print(get_input(i))