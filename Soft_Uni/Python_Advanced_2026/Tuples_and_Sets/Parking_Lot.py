n = int(input())

parking_lot = set()

for _ in range(n):
    command, plate_number = input().split(", ")
    if command == "IN":
        parking_lot.add(plate_number)
    elif command == "OUT":
        parking_lot.remove(plate_number)

if len(parking_lot) == 0:
    print("Parking Lot is Empty")
else:
    for plate in parking_lot:
        print(plate)
        
    