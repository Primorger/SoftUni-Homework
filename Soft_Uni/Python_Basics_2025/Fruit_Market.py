strawberry_cost = float(input())
banana_amount = float(input())
orange_amount = float(input())
raspberry_amount = float(input())
strawberry_amount = float(input())

raspberry_cost = strawberry_cost / 2
orange_cost = raspberry_cost * 0.6
banana_cost = raspberry_cost * 0.2

total_cost = (strawberry_cost * strawberry_amount) + (raspberry_cost * raspberry_amount) + (orange_cost * orange_amount) + (banana_cost * banana_amount)
print(f"{total_cost:.2f}")
