budget = float(input())
num_nights = int(input())
night_cost = float(input())
additional_expenses_percent = float(input())

if num_nights > 7:
    night_cost -= night_cost * 0.05

price_for_trip = num_nights * night_cost
additional_expenses = budget * (additional_expenses_percent / 100)
total_costs = price_for_trip + additional_expenses

diff_sum = abs(total_costs - budget)

if budget >= total_costs:
    print(f"Ivanovi will be left with {diff_sum:.2f} leva after vacation.")
else:
    print(f"{diff_sum:.2f} leva needed.")
