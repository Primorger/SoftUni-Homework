first_strings = input().split(", ")
second_strings = input().split(", ")
sub_strings = []

for first_string in first_strings:
    for second_string in second_strings:
        if first_string in second_string:
            sub_strings.append(first_string)
            break

print(sub_strings)