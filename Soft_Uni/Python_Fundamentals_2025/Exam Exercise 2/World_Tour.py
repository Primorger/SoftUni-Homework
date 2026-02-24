stops = input()

while True:
    command = input()
    if command == "Travel":
        break
    command = command.split(":")
    if command[0] == "Add Stop":
        index, string = int(command[1]), command[2]
        if not (0 <= index <= len(stops)):
            print(stops)
            continue
        stops = stops[:index] + string + stops[index:]      
    elif command[0] == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        if not (0 <= start_index <= end_index < len(stops)):
            print(stops)
            continue
        stops = stops[:start_index] + stops[end_index+1:]       
    elif command[0] == "Switch":
        old_string, new_string = command[1], command[2]
        if not old_string in stops:
            print(stops)
            continue
        stops = stops.replace(old_string, new_string)
    print(stops)      
print(f"Ready for world tour! Planned stops: {stops}")
