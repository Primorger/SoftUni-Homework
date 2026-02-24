budget = float(input())
number_graphics_cards = int(input())
number_processors = int(input())
number_ram = int(input())

cost_graphics_cards = 250 * number_graphics_cards
cost_processors = (0.35 * cost_graphics_cards ) * number_processors
cost_ram = (0.1 * cost_graphics_cards) * number_ram
sum_shopping = cost_graphics_cards + cost_processors + cost_ram

if number_graphics_cards > number_processors:
    sum_shopping -= (sum_shopping * 0.15)

if budget >= sum_shopping:
    print(f"You have {budget - sum_shopping:.2f} leva left!")
    
else:
    print(f"Not enough money! You need {abs(budget - sum_shopping):.2f} leva more!")