money_needed = float(input())
owned_money = float(input())
days = 0
spending_streak = 0

while True:
    action = input()
    money_spent_or_saved = float(input())

    if action == "spend":
        owned_money -= money_spent_or_saved
        if owned_money < 0:
            owned_money = 0
        spending_streak += 1

    elif action == "save":
        owned_money += money_spent_or_saved
        spending_streak = 0
        
    days += 1

    if owned_money >= money_needed:
        print(f"You saved the money for {days} days.")
        break

    if spending_streak == 5:
        print("You can't save the money.")
        print(days)
        break
