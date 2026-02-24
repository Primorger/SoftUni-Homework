# prints "zero" if the number is zero

# - prints "positive" or "negative"

# - adds "small" if the absolute value of the number is less than 1 and it is not 0, or "large" if it exceeds

# 1 000 000

num = float(input())
if num == 0:
    print("zero")

elif num > 0:
    if abs(num) < 1 and num != 0:
        print("small", end=" ")
    elif abs(num) > 1_000_000:
        print("large", end=" ")
    print("positive")
else:
    if abs(num) < 1 and num != 0:
        print("small", end=" ")
    elif abs(num) > 1_000_000:
        print("large", end=" ")
    print("negative")