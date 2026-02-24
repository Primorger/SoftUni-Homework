operator = input()
num_1 = int(input())
num_2 = int(input())

def calculate(op, a, b):

    if op == "add":
        return a + b
    elif op == "subtract":
        return a - b
    elif op == "multiply":
        return a * b
    elif op == "divide":
        return int(a / b)
    
print(calculate(operator, num_1, num_2))