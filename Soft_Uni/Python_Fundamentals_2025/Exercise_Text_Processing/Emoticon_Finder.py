input_str = input()
for i in range(len(input_str)):
    if input_str[i] == ":":
        print(f"{input_str[i]}{input_str[i+1]}")