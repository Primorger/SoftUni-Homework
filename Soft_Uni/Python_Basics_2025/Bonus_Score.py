score = int(input())
bonus_points = int(0)

if score <= 100:
    bonus_points += 5
elif score > 1000:
    bonus_points += (0.1 * score)
else:
    bonus_points += (0.2 * score)

if score % 2 == 0:
    bonus_points += 1
elif score % 10 == 5:
    bonus_points += 2

print(bonus_points)
print(bonus_points + score)