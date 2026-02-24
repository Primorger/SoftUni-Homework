from collections import deque

expression = input().split()
numbers = deque()

operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x // y
}

for chr in expression:
    if chr not in "*-+/":
        numbers.append(int(chr))
    else:
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()

            numbers.appendleft(operators[chr](first_num, second_num))
print(numbers[0])