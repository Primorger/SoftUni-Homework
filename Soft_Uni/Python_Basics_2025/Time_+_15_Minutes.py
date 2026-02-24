hours = int(input())
minutes = int(input()) + 15

while minutes > 59:
    minutes = minutes - 60
    hours += 1
    
if hours > 23:
    hours = 0

if minutes < 10:
    print(f"{hours}:{minutes:02d}")
else:
    print(f"{hours}:{minutes}")