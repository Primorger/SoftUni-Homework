def make_milkshakes(chocolates_input, milk_input):

    chocolates = [int(x) for x in chocolates_input.split(", ")]
    milk = [int(x) for x in milk_input.split(", ")]
    
    milkshakes_made = 0
    
    while milkshakes_made < 5 and chocolates and milk:

        while chocolates and chocolates[-1] <= 0:
            chocolates.pop()

        while milk and milk[0] <= 0:
            milk.pop(0)
        
        if not chocolates or not milk:
            break
        
        if chocolates[-1] == milk[0]:
            chocolates.pop()
            milk.pop(0)
            milkshakes_made += 1
        else:
            milk.append(milk.pop(0))
            chocolates[-1] -= 5
    
    if milkshakes_made == 5:
        print("Great! You made all the chocolate milkshakes needed!")
    else:
        print("Not enough milkshakes.")
    
    if chocolates:
        print(f"Chocolate: {', '.join(map(str, chocolates))}")
    else:
        print("Chocolate: empty")
    
    if milk:
        print(f"Milk: {', '.join(map(str, milk))}")
    else:
        print("Milk: empty")


chocolates_input = input()
milk_input = input()

make_milkshakes(chocolates_input, milk_input)