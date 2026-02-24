days = int(input())
tot_rakia_liters = 0
tot_alcoholic_degrees = 0
for i in range(1, days + 1):
    rakia_liters = float(input())
    alcoholic_degree = float(input())
    tot_rakia_liters += rakia_liters
    tot_alcoholic_degrees += alcoholic_degree * rakia_liters

average_alcoholic_degree = tot_alcoholic_degrees / tot_rakia_liters

print(f"Liter: {tot_rakia_liters:.2f}")
print(f"Degrees: {average_alcoholic_degree:.2f}")

if average_alcoholic_degree < 38:
    print(f"Not good, you should baking!")
elif 38 <= average_alcoholic_degree < 42 :
    print("Super!")
elif 42 <= average_alcoholic_degree:
    print(f"Dilution with distilled water!" )
