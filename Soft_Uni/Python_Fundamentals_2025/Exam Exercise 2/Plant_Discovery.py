n = int(input())
plants = {}
for _ in range(n):
    plant_data = input().split("<->")
    plant_name = plant_data[0]
    plant_rarity = int(plant_data[1])
    plants[plant_name] = {"rarity": plant_rarity, "ratings": []}

while True:
    command = input()
    if command == "Exhibition":
        break
    command_parts = command.split(": ")
    action = command_parts[0]
    details = command_parts[1]

    if action == "Rate":
        plant_name, rating = details.split(" - ")
        rating = float(rating)
        if plant_name in plants:
            plants[plant_name]["ratings"].append(rating)
        else:
            print("error")

    elif action == "Update":
        plant_name, new_rarity = details.split(" - ")
        new_rarity = int(new_rarity)
        if plant_name in plants:
            plants[plant_name]["rarity"] = new_rarity
        else:
            print("error")

    elif action == "Reset":
        plant_name = details
        if plant_name in plants:
            plants[plant_name]["ratings"].clear()
        else:
            print("error")

for plant in plants.values():
    if plant["ratings"]:
        plant["average_rating"] = sum(plant["ratings"]) / len(plant["ratings"])
    else:
        plant["average_rating"] = 0

print("Plants for the exhibition:")

for plant_name, plant_info in plants.items():
    print(f"- {plant_name}; Rarity: {plant_info['rarity']}; Rating: {plant_info['average_rating']:.2f}")
