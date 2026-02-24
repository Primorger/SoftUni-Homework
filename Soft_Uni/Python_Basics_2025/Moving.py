width = int(input())
length = int(input())
height = int(input())

total_space_left = width * length * height
command = input()

while command != "Done":
    space = int(command)
    total_space_left -= space
    if total_space_left <= 0:
        break
    command = input()
if total_space_left < 0:
    print(f"No more free space! You need {abs(total_space_left)} Cubic meters more.")
else:
    print(f"{total_space_left} Cubic meters left.")