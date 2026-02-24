needed_nylon = int(input()) 
needed_paint = int(input())
needed_dilutor = int(input())
needed_time = int(input())

cost_nylon = (needed_nylon + 2) * 1.50
cost_paint = (needed_paint + 0.1 * needed_paint) * 14.50
cost_dilutor = needed_dilutor * 5.00
cost_plastic_bags = 0.40 
cost_for_materials = cost_nylon + cost_paint + cost_dilutor + cost_plastic_bags
cost_for_workers = (0.3 * cost_for_materials) * needed_time
cost_sum = cost_for_materials + cost_for_workers

print(cost_sum)