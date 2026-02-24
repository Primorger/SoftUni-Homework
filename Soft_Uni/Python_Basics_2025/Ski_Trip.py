days = int(input())
room_type = input() #"room for one person", "apartment" или "president apartment"
mood = input()  # "positive" или "negative"

nights = days - 1
discount = 0.0
price_per_night = 0.0
if room_type == "room for one person":
    price_per_night = 18.0
    if nights < 10:
        discount = 0.0
    elif nights <= 15:
        discount = 0.0
    else:
        discount = 0.0
elif room_type == "apartment":
    price_per_night = 25.00
    if nights < 10:
        discount = 0.30
    elif nights <= 15:
        discount = 0.35
    else:
        discount = 0.50
elif room_type == "president apartment":
    price_per_night = 35.00
    if nights < 10:
        discount = 0.10
    elif nights <= 15:
        discount = 0.15
    else:
        discount = 0.20

total_price = price_per_night * nights
total_price_after_discount = total_price * (1 - discount)

if mood == "positive":
    total_price_after_discount *= 1.25
else:
    total_price_after_discount *= 0.90

print(f"{total_price_after_discount:.2f}")