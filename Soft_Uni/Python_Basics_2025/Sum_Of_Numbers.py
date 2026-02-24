anticipated_sum = int(input())
num = int(input())
tot_sum = num
while True:
    num = int(input())
    tot_sum += num
    if tot_sum >= anticipated_sum:
        print(tot_sum)
        break