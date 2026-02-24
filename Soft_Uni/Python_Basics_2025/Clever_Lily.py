age = int(input())
cost_of_washing_machine = float(input())
toy_price = int(input())

saved_money = 0
toy_counter = 0
money_gift = 10

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        saved_money += money_gift
        money_gift += 10
        saved_money -= 1
    else:
        toy_counter += 1

tot_toy_money = toy_counter * toy_price
saved_money += tot_toy_money

diff = saved_money - cost_of_washing_machine

if diff >= 0:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {abs(diff):.2f}")