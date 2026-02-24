n = int(input())

lst = []
special_lst = []

for _ in range(n):
    obj = int(input())
    lst.append(obj)

command = input()

for char in lst:
    if command == "even":
        if char % 2 == 0:
            special_lst.append(char)
    elif command == "odd":
        if char % 2 != 0:
            special_lst.append(char)
    elif command == "negative":
        if char < 0:
            special_lst.append(char)
    elif command == "positive":
        if char >= 0:
            special_lst.append(char)
            
print(special_lst)