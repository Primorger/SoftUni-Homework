numbers = list(input().split())
reversed_numbers = []

while numbers:
    reversed_numbers.append(str(numbers.pop()))

print(" ".join(reversed_numbers))
