input_string = input()
result = ""
strength = 0
for i in range(len(input_string)):
    if strength > 0 and input_string[i] != ">":
        strength -= 1
    elif input_string[i] == ">":
        result += input_string[i]
        strength += int(input_string[i + 1])
    else:
        result += input_string[i]
print(result)