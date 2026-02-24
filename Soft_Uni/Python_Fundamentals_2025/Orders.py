n = int(input())

capsule_price = 0
days = 0
capsules_per_day = 0

full_price = 0

for _ in range(n):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if not (0.01 <= capsule_price <= 100):
        continue
    if not (1 <= days <= 31):
        continue
    if not (1 <= capsules_per_day <= 2000):
        continue

    price = capsule_price * capsules_per_day * days

    full_price += price

    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${full_price:.2f}")