events = input().split("|")
tot_energy = 100
tot_coins = 100
bakery_is_open = True

for event in events:
    
    event_values = event.split("-")

    event_type, event_value = event_values[0], int(event_values[1])

    if event_type == "rest":
        initial_energy = tot_energy
        tot_energy += event_value

        if tot_energy > 100:
            tot_energy = 100
        gained_energy = tot_energy - initial_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {tot_energy}.")

    elif event_type == "order":

        if tot_energy >= 30:
            tot_energy -= 30
            tot_coins += event_value

            print(f"You earned {event_value} coins.")

        else:
            tot_energy += 50
            print("You had to rest!")
    else:
        if tot_coins >= event_value:
            print(f"You bought {event_type}.") 
            tot_coins -= event_value 
        else:
            bakery_is_open = False
            break
if bakery_is_open:
    print("Day completed!")
    print(f"Coins: {tot_coins}")
    print(f"Energy: {tot_energy}")

else:
    print(f"Closed! Cannot afford {event_type}.")