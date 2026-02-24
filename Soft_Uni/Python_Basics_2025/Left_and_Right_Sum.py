n = int(input())
counter1 = 0
counter2 = 0
sum = 0
for times in range(n):
    number = int(input())
    counter1 += number
print("")
sum = counter1
for times in range(n):
    number = int(input())
    counter2 += number
diff = abs(counter1 - counter2)
if counter1 == counter2:
    print(f"Yes, sum = {sum}")
else:
    print(f"No, diff = {diff}")