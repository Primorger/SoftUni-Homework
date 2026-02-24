budget = float(input())     # •	На първи ред – бюджетът - реално число в интервала [1.00… 100000.00]

product_name = ""
items_purchased = []
product_price = float(0)
product = 0

purchase_size = 0

while True:
    product_name = input()
    if product_name == "Stop":
        print(f"You bought {len(items_purchased)} products for {purchase_size:.2f} leva.")
        break
    else:
        items_purchased.append(product_name)

    product_price = float(input())
    if len(items_purchased) % 3 == 0:
        product_price /= 2
    purchase_size += product_price
        
    if purchase_size > budget:
        print("You don't have enough money!")
        print(f"You need {purchase_size - budget:.2f} leva!")
        break
