budget = int(input())

while True:
    purchase = input()
    if purchase == "End":
        print("You bought everything needed.")
        break
    purchase = int(purchase)
    budget -= purchase
    if budget < 0:
        print("You went in overdraft!")
        break