temp_initial = 3.4
height_initial = 405
height_final = 2016

lapse_rate_per_100m = 0.6

temp_final = temp_initial - (lapse_rate_per_100m * abs(height_final - height_initial) / 100)
print(f"{temp_final=:.1f}")