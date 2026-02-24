deposited_sum = int(input())
time_win_deposit = int(input())
prosentage = float(input())

nat_intrest = deposited_sum * (prosentage/100)
intrest_per_month = nat_intrest/12
sum = deposited_sum + time_win_deposit * intrest_per_month
print(sum)