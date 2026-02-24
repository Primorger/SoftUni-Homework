available_sum = 0
data1 = 0.0
data = ""
while True:
    data = input()

    if data == "NoMoreMoney":
        break

    data1 = float(data)

    if data1 >= 0:
        available_sum += data1
        print(f"Increase: {data1:.2f}")
    else:
        print("Invalid operation!")
        break
print(f"Total: {available_sum:.2f}")
