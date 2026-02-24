beggars = []

money = input()
money_given = money.split(", ")

number_of_beggars = int(input())

for _ in range(number_of_beggars):
    beggars.append(0)

for i in range(len(money_given)):
    beggars[i % number_of_beggars] += int(money_given[i]) 

print(beggars)