num_of_tournaments = int(input())
starting_points = int(input())

tot_points = starting_points
points_earned = 0
wins = 0

for _ in range(num_of_tournaments):
    result = input()

    if result == "W":
        tot_points += 2000
        points_earned += 2000
        wins += 1
    elif result == "F":
        tot_points +=1200
        points_earned += 1200
    elif result == "SF":
        tot_points += 720
        points_earned += 720

average_points = points_earned // num_of_tournaments
wins_persentage = (wins / num_of_tournaments) * 100

print(f"Final points: {tot_points}")
print(f"Average points: {average_points}")
print(f"{wins_persentage:.2f}%")