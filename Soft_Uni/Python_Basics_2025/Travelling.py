money_collected = 0.0
end = True
while end:
    command = input()
    if command == "End":
        end = False
        break
    money_needed = float(input())
    destination = command
    while not (money_collected >= money_needed):
        money_collected += float(input())
    print(f"Going to {destination}!")
    money_collected = 0.0