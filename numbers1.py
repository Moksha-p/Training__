def prime_numbers_between(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

print(prime_numbers_between(10, 30))  # Output: [11, 13, 17, 19, 23, 29]
