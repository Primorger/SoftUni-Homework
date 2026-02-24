import os

stay_length = int(input("Enter the length of your stay: "))

shirts = stay_length
pants = stay_length + 2
trousers = stay_length
socks = stay_length + 2

items_needed = ("sh", "tr", "pa", "so")
item_list = [shirts, trousers, pants, socks]

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

while any(item != 0 for item in item_list):
    item_packed = input()

    while item_packed not in items_needed:
        print(f'"{item_packed}" is not a valid item!')
        item_packed = input()

    if item_packed == items_needed[0]:
        item_list[0] -= 1
    elif item_packed == items_needed[1]:
        item_list[1] -= 1
    elif item_packed == items_needed[2]:
        item_list[2] -= 1
    elif item_packed == items_needed[3]:
        item_list[3] -= 1

    for i in range(len(item_list)):
        if item_list[i] < 0:
            item_list[i] = 0

    clear_terminal()
    print(f"shirts needed:   {item_list[0]}")
    print(f"trousers needed: {item_list[1]}")
    print(f"pants needed:    {item_list[2]}")
    print(f"socks needed:    {item_list[3]}")

print()
print("You have finished packing!")