n = int(input())

for _ in range(n):
    num = int(input())
    # · If the number is 88 - "Hello"
    if num == 88:
        print("Hello")
    # · If the number is 86 - "How are you?"
    elif num == 86:
        print("How are you?")
    # · If the number is not 88 nor 86, and it is below 88 - "GREAT!"
    elif num < 88:
        print("GREAT!")
    # · If the number is over 88 - "Bye."
    elif num > 88:
        print("Bye.")