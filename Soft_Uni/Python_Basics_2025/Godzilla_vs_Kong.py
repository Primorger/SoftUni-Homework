budget = float(input())
statists = int(input())
price_per_statist = float(input())

decore_price = budget * 0.1
clothes_price = price_per_statist * statists

if statists > 150:
    clothes_price -= (clothes_price * 0.1)

needed_money = decore_price + clothes_price

if needed_money > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {needed_money - budget:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {budget - needed_money:.2f} leva left.")