math_expression = input()

stack = []

for i in range(len(math_expression)):
    if math_expression[i] == "(":
        stack.append(i)
        
    elif math_expression[i] == ")":
        start_index = stack.pop()
        end_index = i + 1

        print(math_expression[start_index:end_index])