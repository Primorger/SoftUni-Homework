heroes = {}
number_of_heroes = int(input())
for current_hero in range(number_of_heroes):
    hero_name, hero_hp, hero_mp = input().split()
    hero_hp = int(hero_hp)
    hero_mp = int(hero_mp)
    heroes[hero_name] = {"HP": hero_hp, "MP": hero_mp}

command = input()
while command != "End":
    command = command.split(" - ")
    action = command[0]
    hero_name = command[1]

    if action == "CastSpell":
        mp_needed = int(command[2])
        spell_name = command[3]
        if heroes[hero_name]["MP"] >= mp_needed:
            heroes[hero_name]["MP"] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        heroes[hero_name]["HP"] -= damage
        if heroes[hero_name]["HP"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
        else:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif action == "Recharge":
        amount = int(command[2])
        current_mp = heroes[hero_name]["MP"]
        heroes[hero_name]["MP"] += amount
        if heroes[hero_name]["MP"] > 200:
            heroes[hero_name]["MP"] = 200
        recharged_amount = heroes[hero_name]["MP"] - current_mp
        print(f"{hero_name} recharged for {recharged_amount} MP!")

    elif action == "Heal":
        amount = int(command[2])
        current_hp = heroes[hero_name]["HP"]
        heroes[hero_name]["HP"] += amount
        if heroes[hero_name]["HP"] > 100:
            heroes[hero_name]["HP"] = 100
        healed_amount = heroes[hero_name]["HP"] - current_hp
        print(f"{hero_name} healed for {healed_amount} HP!")

    command = input()
    
for hero, stats in heroes.items():
    print(f"{hero}")
    print(f"  HP: {stats['HP']}")
    print(f"  MP: {stats['MP']}")
