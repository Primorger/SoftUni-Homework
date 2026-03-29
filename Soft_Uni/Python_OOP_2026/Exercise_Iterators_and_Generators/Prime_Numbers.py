def get_primes(nums):
    def is_prime(n):
        if n < 2: return False
        return all(n % i for i in range(2, int(n**0.5) + 1))
            
    for num in nums:
        if is_prime(num):
            yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))