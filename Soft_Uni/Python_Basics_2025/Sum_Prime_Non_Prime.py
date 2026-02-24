num = input()

sum_prime_numbers = 0
sum_non_prime_numbers = 0
while num != "stop":
    num = int(num)
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if num < 0:
        print("Number is negative.")
        num = input()
        continue

    if prime:
        sum_prime_numbers += num
    else:
        sum_non_prime_numbers += num
    

    num = input()

print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")