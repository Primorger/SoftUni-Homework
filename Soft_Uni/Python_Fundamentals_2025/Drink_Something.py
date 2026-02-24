age = int(input())

def drink_somthing(a):
    if a <= 14:
        return "toddy"
    elif a <= 18:
        return "coke"
    elif a <= 21:
        return "beer"
    else:
        return "whisky"

print("drink " + drink_somthing(age))