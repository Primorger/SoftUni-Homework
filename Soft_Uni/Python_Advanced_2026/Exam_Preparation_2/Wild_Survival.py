bee_groups = [int(x) for x in input().split()]
bee_eater_groups = [int(x) for x in input().split()]

while True:
    if not bee_groups or not bee_eater_groups:
        break

    while True:
        if bee_groups[0] == 0 and bee_eater_groups[-1] == 0:
            bee_eater_groups.pop(-1)
            bee_groups.pop(0)
            
        if not bee_groups or not bee_eater_groups:
            break

        if bee_eater_groups[-1] == 0:          
            bee_eater_groups.pop(-1)
            bee_groups.append(bee_groups.pop(0))
            break

        if bee_groups[0] == 0:
            bee_groups.pop(0)
            break

        if bee_groups[0] >= 7:
            bee_groups[0] -= 7
            bee_eater_groups[-1] -= 1

        elif bee_groups[0] < 7:
            bee_groups[0] = 0

print("The final battle is over!")
if not bee_groups and not bee_eater_groups:
    print("But no one made it out alive!")
elif not bee_eater_groups:
    print(f"Bee groups left: {', '.join(map(str, bee_groups))}")
elif not bee_groups:
    print(f"Bee-eater groups left: {', '.join(map(str, bee_eater_groups))}")