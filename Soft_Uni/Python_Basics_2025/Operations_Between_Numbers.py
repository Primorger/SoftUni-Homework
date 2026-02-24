num1 = int(input())
num2 = int(input())
operator = str(input())
result = 0
odd_or_even = ""

if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        result = (num1 + num2)
        if (result % 2) == 0:
            odd_or_even = "even"
        else:
            odd_or_even = "odd"
    if operator == "-":
        result = (num1 - num2)
        if (result % 2) == 0:
            odd_or_even = "even"
        else:
            odd_or_even = "odd"
    if operator == "*":
        result = (num1 * num2)
        if (result % 2) == 0:
            odd_or_even = "even"
        else:
            odd_or_even = "odd"
    print(f"{num1} {operator} {num2} = {result} - {odd_or_even}")

elif operator == "/":
    if num1 == 0 or num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        result =  (num1 / num2)
        print(f"{num1} / {num2} = {result:.2f}")

elif operator == "%":
    if num1 == 0 or num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        result = (num1 % num2)
        print(f"{num1} % {num2} = {result}")
