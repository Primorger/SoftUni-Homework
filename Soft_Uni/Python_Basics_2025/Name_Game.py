player_one_points = 0
player_two_points = 0
player_flag = 0
while True:
    player_name = input()
    player_flag += 1
    if player_flag == 3:
        break
    if player_name == "Stop":
        break
    for i in player_name:
        ascii_letter = int(input())
        if player_flag == 1:
            player_one_name = player_name
            if ord(i) == ascii_letter:
                player_one_points += 10
            else:
                player_one_points += 2
        elif player_flag == 2:
            player_two_name = player_name
            if ord(i) == ascii_letter:
                player_two_points += 10
            else:
                player_two_points += 2
if player_one_points > player_two_points:
    print(f"The winner is {player_one_name} with {player_one_points} points!")
elif player_one_points < player_two_points:
    print(f"The winner is {player_two_name} with {player_two_points} points!")
elif player_one_points == player_two_points:
    print(f"The winner is {player_two_name} with {player_two_points} points!")