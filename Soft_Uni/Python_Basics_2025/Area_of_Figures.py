from math import pi
SHAPE = str(input())

if SHAPE == "square":
    side = float(input())
    square_area = side * side

    print(f"{square_area:.3f}")

elif SHAPE == "rectangle":
    side1 = float(input())
    side2 = float(input())
    rectagle_area = side1 * side2

    print(f"{rectagle_area:.3f}")


elif SHAPE == "circle":
    radius = float(input())
    circle_area = (radius * radius) * pi

    print(f"{circle_area:.3f}")

elif SHAPE == "triangle":
    side = float(input())
    height = float(input())
    triangle_area = (side * height) / 2

    print(f"{triangle_area:.3f}")