steps_goal = 10000
command = input()
steps_counter = 0
going_home = False

while command != "Going home":
    steps = int(command)
    steps_counter += steps

    if steps_counter >= steps_goal:
        break

    command = input()


if command == "Going home":
    steps = int(input())
    steps_counter += steps

if steps_counter >= steps_goal:
    print(f"Goal reached! Good job!")
    print(f"{steps_counter - steps_goal} steps over the goal!")
else:
    print(f"{abs(steps_goal - steps_counter)} more steps to reach goal.")

