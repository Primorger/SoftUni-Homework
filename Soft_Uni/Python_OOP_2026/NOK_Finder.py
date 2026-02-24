num1 = int(input())
num2 = int(input())

if num1 > num2:
    nok = num1
else:
    nok = num2

def check_nok(num1, num2, nok):
    while True:
        if nok % num1 == 0 and nok % num2 == 0:
            return nok
        nok += 1

result = check_nok(num1, num2, nok)

print(result)

print(f"[{num1} * {int(result/num1)} = {result}]")
print(f"[{num2} * {int(result/num2)} = {result}]")