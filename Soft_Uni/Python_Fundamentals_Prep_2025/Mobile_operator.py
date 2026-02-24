contract_length = input()           # Срок на договор – текст – "one", или "two"
contract_type = input()             # Тип на договор – текст – "Small",  "Middle", "Large"или "ExtraLarge"
mobile_internet = input()           # Добавен мобилен интернет – текст – "yes" или "no"
months_of_payment = int(input())    # Брой месеци за плащане - цяло число в интервала [1 … 24]

if contract_length == "one":
    if contract_type == "Small":
        price_per_month = 9.98
    elif contract_type == "Middle":
        price_per_month = 18.99
    elif contract_type == "Large":
        price_per_month = 25.98
    else:
        price_per_month = 35.99
else:
    if contract_type == "Small":
        price_per_month = 8.58
    elif contract_type == "Middle":
        price_per_month = 17.09
    elif contract_type == "Large":
        price_per_month = 23.59
    else:
        price_per_month = 31.79

if mobile_internet == "yes":
    if price_per_month <= 10:
        price_per_month += 5.5
    elif price_per_month <= 30:
        price_per_month += 4.35
    else:
        price_per_month += 3.85

final_price = price_per_month * months_of_payment

if contract_length == "two":
    final_price -= final_price * (0.0375)

print(f"{final_price:.2f} lv.")