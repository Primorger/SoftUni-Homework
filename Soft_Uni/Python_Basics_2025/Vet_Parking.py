days = int(input())
hours = int(input())
parking_cost = 0
total_parking_cost = 0
for day in range(1, days + 1):
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            parking_cost += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            parking_cost += 1.25
        else:
            parking_cost += 1

    print(f"Day: {day} - {parking_cost:.2f} leva")
    total_parking_cost += parking_cost
    parking_cost = 0     
print(f"Total: {total_parking_cost:.2f} leva")