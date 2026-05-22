num1 = int(input())
num2 = int(input())

def check_nok(num1: int, num2: int) -> int:
    nok = max(num1, num2)
    while True:
        if nok % num1 == 0 and nok % num2 == 0:
            return nok
        nok += 1

result = check_nok(num1, num2)

print(result)

print(f"[{num1} * {int(result/num1)} = {result}]")
print(f"[{num2} * {int(result/num2)} = {result}]")