days_of_adventure = int(input())
number_of_adventurers = int(input())
initial_energy = float(input())
water_per_person_per_day = float(input())
food_per_person_per_day = float(input())

food_for_journey = (food_per_person_per_day * number_of_adventurers) * days_of_adventure
water_for_journey = (water_per_person_per_day * number_of_adventurers) * days_of_adventure
current_food = food_for_journey
current_water = water_for_journey
energy = initial_energy

for day in range(1, days_of_adventure + 1):
    daily_energy_loss = float(input())
    energy -= daily_energy_loss
    if energy <= 0:
        print(f"You will run out of energy. You will be left with {current_food:.2f} food and {current_water:.2f} water.")
        break
    if day % 2 == 0:
        energy += energy * 0.05
        current_water -= current_water * 0.30
    if day % 3 == 0:
        energy += energy * 0.10
        food_lost = current_food/number_of_adventurers
        current_food -= food_lost
else:
    print(f"You are ready for the quest. You will be left with {energy:.2f} energy!")