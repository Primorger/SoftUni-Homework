floors = int(input())
rooms = int(input())
room_string = ''
for floor_num in range(floors, 0, -1):
    for room_num in range(rooms):
        if floor_num == floors:
            room_string = f"L{floor_num}{room_num}"
        elif floor_num % 2 ==  0:
            room_string = f"O{floor_num}{room_num}" 
        elif floor_num % 2 !=  0:
            room_string = f"A{floor_num}{room_num}"

        print(room_string, end=" ")
    print()