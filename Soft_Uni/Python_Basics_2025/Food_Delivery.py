chicken_menus = int(input())
fish_menus = int(input())
vegan_menus = int(input())

cost_for_chicken_menus = chicken_menus * 10.35
cost_for_fish_menus = fish_menus * 12.40
cost_for_vegan_menus = vegan_menus * 8.15
whole_cost_for_menus = cost_for_chicken_menus + cost_for_fish_menus + cost_for_vegan_menus
cost_for_deserts = 0.2 * whole_cost_for_menus
cost_of_delivery = 2.50
entire_cost_for_orders = whole_cost_for_menus + cost_for_deserts + cost_of_delivery

print(entire_cost_for_orders)