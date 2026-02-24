import re
bought_furniture = []
tot_cost = 0
pattern = fr">>([a-z]+)<<(\d+\.?\d*)!(\d+)"
while True:
    command = input()
    if command == "Purchase":
        break
    match = re.search(pattern, command, re.IGNORECASE)
    try:
        furniture_name, price, furniture_qt = match.groups()
        bought_furniture.append(furniture_name)
        tot_cost += float(price) * int(furniture_qt)
    except:
        continue
print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {tot_cost:.2f}")