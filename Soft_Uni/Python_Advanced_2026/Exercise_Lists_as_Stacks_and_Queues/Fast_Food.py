from collections import deque

quantity_of_food = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))

while orders and orders[0] <= quantity_of_food:
    quantity_of_food -= orders.popleft()
    if not orders:
        break

if orders:
    print("Orders left:", end=" ")
    print(*orders)
else:
    print("Orders complete")