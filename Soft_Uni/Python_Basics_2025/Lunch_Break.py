from math import ceil
series_name = input()
duration_episode = int(input())
break_duration = int(input())

lunch_duration = break_duration / 8
time_for_break = break_duration / 4
time_left = break_duration - (duration_episode + lunch_duration + time_for_break)

if time_left >= 0:
    print(f"You have enough time to watch {series_name} and left with {ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(abs(time_left))} more minutes.")