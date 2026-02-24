actor_name = input()
academy_points = float(input())
number_of_judges = int(input())

judge_name = ""
points_from_judge = 0.0
final_points = academy_points

for _ in range(number_of_judges):
    judge_name = input()
    points_from_judge = float(input())
    final_points += ((len(judge_name) * points_from_judge) / 2)
    if final_points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {(final_points):.1f}!")
        break
 
else:
    print(f"Sorry, {actor_name} you need {(1250.5 - final_points):.1f} more!")