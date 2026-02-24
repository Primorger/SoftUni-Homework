vacation_cost = float(input())

number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

num_toys = number_puzzles + number_dolls + number_bears + number_minions + number_trucks
sum_toys = (number_puzzles * 2.6) + (number_dolls * 3) + (number_bears * 4.1) + (number_minions * 8.2) + (number_trucks * 2)

if num_toys >= 50:
    sum_toys -= (sum_toys * 0.25)

sum_toys -= (sum_toys * 0.1)

if sum_toys >= vacation_cost:
    print(f"Yes! {sum_toys - vacation_cost:.2f} lv left.")
else:
    print(f"Not enough money! {vacation_cost - sum_toys:.2f} lv needed.")