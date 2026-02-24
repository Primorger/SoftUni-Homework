week_days = [2.50, 1.20, 0.85, 1.45, 2.70, 5.50, 3.85]
weekend = [2.70, 1.25, 0.90, 1.60, 3.00, 5.60, 4.20]
product = input()
day = input()
amount = float(input())
item_cost = 0
ERROR_DATA = False

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if product == "banana" :
        item_cost = week_days[0] * amount
    elif product == "apple":
        item_cost = week_days[1] * amount
    elif product == "orange":
        item_cost = week_days[2] * amount
    elif product == "grapefruit":
        item_cost = week_days[3] * amount
    elif product == "kiwi":
        item_cost = week_days[4] * amount
    elif product == "pineapple":
        item_cost = week_days[5] * amount
    elif product == "grapes":
        item_cost = week_days[6] * amount
    else:
        ERROR_DATA = True
        
elif day == "Saturday" or day == "Sunday":
    if product == "banana" :
        item_cost = weekend[0] * amount
    elif product == "apple":
        item_cost = weekend[1] * amount
    elif product == "orange":
        item_cost = weekend[2] * amount
    elif product == "grapefruit":
        item_cost = weekend[3] * amount
    elif product == "kiwi":
        item_cost = weekend[4] * amount
    elif product == "pineapple":
        item_cost = weekend[5] * amount
    elif product == "grapes":
        item_cost = weekend[6] * amount
    else:
        ERROR_DATA = True
else:
    ERROR_DATA = True

if ERROR_DATA == True:
    print("error")
else:
    print(f"{item_cost:.2f}")

