# Write a Python program to find all the prime numbers between two given numbers.

def find_primes_between_range(start, end):
    prime_list = []
    for number in range(start, end + 1):
        if number > 1:  
            is_prime = True
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:  
                    is_prime = False
                    break
            if is_prime:
                prime_list.append(number)
    return prime_list

# Example Test Case:
start = 10
end = 30
print(find_primes_between_range(start, end))


# Write a Python program to find the first n numbers that are both prime.

def get_first_n_primes(n):
    prime_num = []
    num = 2  
    while len(prime_num) < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:  
                is_prime = False
                break
        if is_prime:
            prime_num.append(num)
        num += 1
    return prime_num

# Example Test Case:
print(get_first_n_primes(5))
