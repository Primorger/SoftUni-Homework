budget = float(input())
destination = input()
season = input()
number_of_days = int(input())

costs = 0

if season == "Winter":
    if destination == "Dubai":
        costs_per_day = 45_000
    elif destination == "Sofia":
        costs_per_day = 17_000
    elif destination == "London":
        costs_per_day = 24_000
elif season == "Summer":
    if destination == "Dubai":
        costs_per_day = 40_000
    elif destination == "Sofia":
        costs_per_day = 12_500
    elif destination == "London":
        costs_per_day = 20_250

costs = costs_per_day * number_of_days

if destination == "Dubai":
    costs -= costs * 0.30
elif destination == "Sofia":
    costs += costs * 0.25

diff = abs(budget - costs)

if budget >= costs:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")