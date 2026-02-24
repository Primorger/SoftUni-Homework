num = int(input())

def perfect_number(number):
    if number <= 0:
        return "It's not so perfect."
    
    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i

    if divisors_sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

print(perfect_number(num))