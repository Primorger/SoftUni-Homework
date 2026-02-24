# 1.	Брой екскурзии за море – цяло число в интервала [1… 500]
excoursion_sea = int(input())
# 2.	Брой екскурзии за планина – цяло число в интервала [1… 500]
excoursion_mountain = int(input())
profit = 0
while True:
    command = input()
    if command == "Stop" or (excoursion_mountain <= 0 and excoursion_sea <= 0):
        break
    if command == "sea":
        if not excoursion_sea <= 0:
            profit += 680
        excoursion_sea -= 1
    elif command == "mountain":
        if not excoursion_mountain <= 0:
            profit += 499
        excoursion_mountain -= 1
    if command == "Stop" or (excoursion_mountain <= 0 and excoursion_sea <= 0):
        break

if excoursion_mountain <= 0 and excoursion_sea <= 0:
    print("Good job! Everything is sold.")
print(f"Profit: {profit} leva.")