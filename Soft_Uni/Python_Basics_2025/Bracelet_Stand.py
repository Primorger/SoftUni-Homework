# •	Първи ред – джобните на Тереза на ден – реално число в интервала [1.00 ...100.00]
allowance_per_day = float(input())
# •	Втори ред – парите, които тя печели на ден от продажби – реално число в интервала [1.00...1000.00]
money_from_sales = float(input())
# •	Трети ред – разходите на Тереза за целия период – реално число в интервала [1.00...1000.00]
expences = float(input())
# •	Четвърти ред – цената на подаръка – реално число в интервала [1.00...10000.00]
order_price = float(input())
days = 5
allowance_saved = days * allowance_per_day
sales_saved = days * money_from_sales
tot_saved_money = (allowance_saved + sales_saved) - expences
diff = abs(tot_saved_money - order_price)
if tot_saved_money >= order_price:
    print(f"Profit: {tot_saved_money:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {diff:.2f} BGN.")