string1 = input()
string2 = input()

str1 = []
str2 = []

def init_list(str, string):
    for char in string:
        str.append(char)

def list_to_str(a):
    output = ""
    for item in a:
        output += item
    return output

init_list(str1, string1)
init_list(str2, string2)

for i in range(len(str1)):
    last_str = str1.copy()
    str1[i] = str2[i]

    if last_str != str1:
        print(list_to_str(str1))
