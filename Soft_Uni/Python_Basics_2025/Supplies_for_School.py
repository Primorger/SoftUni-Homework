num_pens = int(input())
num_markers = int(input())
liters_cleaning_fluid = int(input())
discount = int(input())

discount_prosentage = discount/100

cost_pens = num_pens * 5.8
cost_markers = num_markers * 7.2
cost_cleaning_fluid = liters_cleaning_fluid * 1.2 
whole_cost = cost_pens + cost_markers + cost_cleaning_fluid
whole_cost_with_discount = whole_cost - (whole_cost * discount_prosentage)

print(whole_cost_with_discount)