SPEED = float(input())

if SPEED <= 10:
    print("slow")
elif 10 < SPEED <= 50:
    print("average")
elif 50 < SPEED <= 150:
    print("fast")
elif 150 < SPEED <= 1000:
    print("ultra fast")
else:
    print("extremely fast")