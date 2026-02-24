travel_route = input().split("||")
initial_fuel = int(input())
initial_ammo = int(input())

current_fuel = initial_fuel
current_ammo = initial_ammo

for current_answer in travel_route:
    if current_answer == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
    answer = current_answer.split()
    command, amount = answer[0], int(answer[1])

    if command == "Travel":
        if amount > current_fuel:
            print("Mission failed.")
            break
        current_fuel -= amount
        print(f"The spaceship travelled {amount} light-years.")
    elif command == "Enemy":
        if current_ammo >= amount:
            current_ammo -= amount
            print(f"An enemy with {amount} armour is defeated.")
        elif current_fuel >= amount * 2:
            current_fuel -= amount * 2
            print(f"An enemy with {amount} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break
    elif command == "Repair":
        current_ammo += amount * 2
        current_fuel += amount
        print(f"Ammunitions added: {amount * 2}.")
        print(f"Fuel added: {amount}.")