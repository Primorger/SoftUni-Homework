def paint_colors(input_string):
    substrings = input_string.split()
    main_colors = {"red", "yellow", "blue"}
    secondary_colors = {
        "orange": {"red", "yellow"},
        "purple": {"red", "blue"},
        "green": {"yellow", "blue"},
    }

    found_colors = []

    while substrings:
        if len(substrings) > 1:
            first = substrings.pop(0)
            last = substrings.pop()
        else:
            first = substrings.pop()
            last = ""

        combined1 = first + last
        combined2 = last + first

        if combined1 in main_colors or combined1 in secondary_colors:
            found_colors.append(combined1)
        elif combined2 in main_colors or combined2 in secondary_colors:
            found_colors.append(combined2)
        else:
            first = first[:-1]
            last = last[:-1]

            middle = len(substrings) // 2
            if first:
                substrings.insert(middle, first)
                middle += 1
            if last:
                substrings.insert(middle, last)

    valid_colors = []
    collected_mains = set(c for c in found_colors if c in main_colors)

    for color in found_colors:
        if color in main_colors:
            valid_colors.append(color)
        else:
            if secondary_colors[color].issubset(collected_mains):
                valid_colors.append(color)

    return valid_colors


input_line = input()
print(paint_colors(input_line))
