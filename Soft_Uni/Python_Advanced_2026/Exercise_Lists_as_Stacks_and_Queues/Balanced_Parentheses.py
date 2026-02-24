expression = input()

parentheses = {"(": ")", "[": "]", "{": "}"}


stack = []

for char in expression:
    if char in parentheses:
        stack.append(char)
    elif char in parentheses.values():
        if not stack or parentheses[stack.pop()] != char:
            print("NO")
            break
else:
    print("YES")