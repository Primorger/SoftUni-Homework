items_bought = input().split("|")

for item in items_bought:
    item_type, item_price = item.split("->")
    item_price = float(item_price)
    