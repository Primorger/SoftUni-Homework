n = int(input())

for _ in range(n):
    command_parts = input().split("-")
    first_range = set(range(int(command_parts[0].split(",")[0]), int(command_parts[0].split(",")[1]) + 1))
    second_range = set(range(int(command_parts[1].split(",")[0]), int(command_parts[1].split(",")[1]) + 1))

    intersection = first_range & second_range
    
    if _ == 0:
        longest_intersection = intersection
    else:
        if len(intersection) > len(longest_intersection):
            longest_intersection = intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")