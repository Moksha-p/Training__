def first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

print(first_n_primes(5))  # Output: [2, 3, 5, 7, 11]
