#Write a Python program to find all the prime numbers between two given numbers.
def primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes
start = 10
end = 30
print(primes(start,end))

# Write a Python program to find the first n numbers that are both prime.
def primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes


print(primes(5))