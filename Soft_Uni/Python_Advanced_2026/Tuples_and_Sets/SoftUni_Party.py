guests_invited = int(input())

guests = set()

for _ in range(guests_invited):
    guest_code = input()
    guests.add(guest_code)

while True:
    command = input()
    if command == "END":
        break
    guests.remove(command)

print(len(guests))
sorted_guests = sorted(guests)

for guest in sorted_guests:
    print(guest)