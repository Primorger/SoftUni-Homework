substance_q = [int(x) for x in input().split(", ")]
crystal_e = [int(x) for x in input().split(", ")]

potions = {
    "Brew of Immortality": 110,
    "Essence of Resilience": 100,
    "Draught of Wisdom": 90,
    "Potion of Agility": 80,
    "Elixir of Strength": 70
}

crafted_potions = []

while substance_q and crystal_e:
    crafted = False

    if len(crafted_potions) == len(potions):
        break
    if not substance_q or not crystal_e:
        break

    energy = substance_q[-1] + crystal_e[0]

    for potion, energy_req in potions.items():
        if energy == energy_req and potion not in crafted_potions:
            crafted_potions.append(potion)
            substance_q.pop(-1)
            crystal_e.pop(0)
            crafted = True
            break
    
    if crafted:
        continue
    
    best_potion = None
    best_energy = None

    for potion, energy_req in potions.items():
        if energy_req < energy and potion not in crafted_potions:
            if best_energy is None or energy_req > best_energy:
                best_potion = potion
                best_energy = energy_req
    
    if best_potion:
        crafted_potions.append(best_potion)
        substance_q.pop(-1)

        removed_crystal = crystal_e.pop(0)
        if removed_crystal - 20 > 0:
            crystal_e.append(removed_crystal - 20)
    else:
        substance_q.pop(-1)

        removed_crystal = crystal_e.pop(0)
        if removed_crystal - 5 > 0:
            crystal_e.append(removed_crystal - 5)

if len(crafted_potions) == len(potions):
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted_potions:
    print(f"Crafted potions: {', '.join(crafted_potions)}")

if substance_q:
    print(f"Substances: {', '.join(map(str, reversed(substance_q)))}")
if crystal_e:
    print(f"Crystals: {', '.join(map(str, crystal_e))}")