amount_for_return = float(input())
amount_returned = 0
while amount_for_return > 0:
    if amount_for_return >= 2:
        amount_for_return -= 2
    elif amount_for_return >= 1:
        amount_for_return -= 1
    elif amount_for_return >= 0.50:
        amount_for_return -= 0.50
    elif amount_for_return >= 0.20:
        amount_for_return -= 0.20
    elif amount_for_return >= 0.10:
        amount_for_return -= 0.10
    elif amount_for_return >= 0.05:
        amount_for_return -= 0.05
    elif amount_for_return >= 0.02:
        amount_for_return -= 0.02
    elif amount_for_return >= 0.01:
        amount_for_return -= 0.01
    amount_returned += 1
    amount_for_return = round(amount_for_return, 2)

print(amount_returned)