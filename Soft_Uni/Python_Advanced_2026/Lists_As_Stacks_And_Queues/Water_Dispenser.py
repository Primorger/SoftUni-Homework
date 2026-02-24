from collections import deque

water_quantity = int(input())
people = deque()

line = input()

while line != "Start":
    people.append(line)
    line = input()


while line != "End":
    line = input()
    if line == "End":
        break
    if line.isdigit():
        person = people.popleft()
        water_needed = int(line)
        if water_needed <= water_quantity:
            water_quantity -= water_needed
            print(f"{person} got water")
        else:
            print(f"{person} must wait")
    else:
        water_quantity += int(line.split()[1])
    

print(f"{water_quantity} liters left")