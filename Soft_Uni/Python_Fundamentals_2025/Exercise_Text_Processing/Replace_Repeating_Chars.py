input_string = input()
result = ""
for char in input_string:
    if not result or char != result[-1]:
        result += char
print(result)