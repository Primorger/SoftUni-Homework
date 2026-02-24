# Тегло на пратката в килограми – реално число в интервала [0.01 ... 150.00]
order_weight = float(input())
# Тип услуга –  текст със следните възможности: "standard" или "express"
service = input()
# Разстояние в километри – цяло число в интервала [1 ... 1000]
distance = float(input())
price = 0

if service == "standard":
    if order_weight < 1:
        price = 0.03
    elif 1 <= order_weight < 10:
        price = 0.05
    elif 10 <= order_weight < 40:
        price = 0.10
    elif 40 <= order_weight < 90:
        price = 0.15
    elif 90 <= order_weight < 150:
        price = 0.20
    final_cost = distance * price
elif service == "express":
    if order_weight < 1:
        price = 0.03
        price_persentage = 0.80
    elif 1 <= order_weight < 10:
        price = 0.05
        price_persentage = 0.40
    elif 10 <= order_weight < 40:
        price = 0.10
        price_persentage = 0.05
    elif 40 <= order_weight < 90:
        price = 0.15
        price_persentage = 0.02
    elif 90 <= order_weight < 150:
        price = 0.20
        price_persentage = 0.01
    price_persentage = price * price_persentage
    nadtsenka = price_persentage * order_weight
    extra_discount = (distance * nadtsenka) 
    cost = distance * price 
    final_cost = extra_discount + cost

print(f"The delivery of your shipment with weight of {order_weight:.3f} kg. would cost {final_cost:.2f} lv.")
    
