from collections import deque

kids = deque(input().split())

step = int(input())

while len(kids) > 1:
    kids.rotate(-step + 1)
    eliminated_kid = kids.popleft()
    print(f"Removed {eliminated_kid}")

print(f"Last is {kids.pop()}")