budget = float(input())
fuel_needed = float(input())
day_of_week = input()

cost_for_fuel = fuel_needed * 2.10
cost_for_guide = 100
tot_money = cost_for_fuel + cost_for_guide
if day_of_week == "Saturday":
    tot_money = tot_money * (1 - 0.10)
else:
    tot_money = tot_money * (1 - 0.20)
diff = budget - tot_money
if diff >= 0:
    print(f"Safari time! Money left: {diff:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {abs(diff):.2f} lv.")