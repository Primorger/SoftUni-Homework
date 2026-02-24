one_eggs = int(input())
two_eggs = int(input())
broken = True
while True:
    command = input()

    if command == "End":
        break
    elif command == "one":
        two_eggs -= 1
    elif command == "two":
        one_eggs -= 1
    if one_eggs == 0 or two_eggs == 0:
        broken = False
        break
    
if not broken:    
    if one_eggs > 0:
        print(f"Player two is out of eggs. Player one has {one_eggs} eggs left.")
    else:
        print(f"Player one is out of eggs. Player two has {two_eggs} eggs left.")
else:
    print(f"Player one has {one_eggs} eggs left.")
    print(f"Player two has {two_eggs} eggs left.")