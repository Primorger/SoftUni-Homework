annual_tax = int(input())

cost_for_sneakers = annual_tax - (annual_tax * 0.4)
cost_for_uniform = cost_for_sneakers - (cost_for_sneakers * 0.2)
cost_for_ball = 0.25 * cost_for_uniform
cost_for_accessories = 0.2 * cost_for_ball
whole_cost_for_equipment = annual_tax + cost_for_sneakers + cost_for_uniform + cost_for_ball + cost_for_accessories

print(whole_cost_for_equipment)