# 1. If Statements

# Write a Python program to classify a given year as a leap year or a non-leap year.

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Non-Leap Year"

# Example Test case
year = 2020
print(check_leap_year(year))  

# Write a Python program to solve a quadratic equation (ax^2 + bx + c = 0) and classify the roots as real, complex, or equal.

import cmath

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        return f"Real roots: {root1.real}, {root2.real}"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"Equal roots: {root}"
    else:
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        return f"Complex roots: {root1}, {root2}"

# Example Test case
a, b, c = 1, -3, 2
print(solve_quadratic(a, b, c))  

# 2. For Loops

# Write a Python function to generate the Fibonacci series up to a given number of terms.

def fibonacci_series(terms):
    fib = [0, 1]
    while len(fib) < terms:
        fib.append(fib[-1] + fib[-2])
    return fib[:terms]

# Example Test case
terms = 5
print(fibonacci_series(terms))  

# Write a Python program to find the longest increasing subsequence in a given list of numbers.

def longest_increasing_subsequence(nums):
    n = len(nums)
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    max_lis = max(lis)
    subsequence = []
    for i in range(n-1, -1, -1):
        if lis[i] == max_lis:
            subsequence.insert(0, nums[i])
            max_lis -= 1
    return subsequence

# Example Test case
nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longest_increasing_subsequence(nums))  

# 3. While Loops

# Write a Python program to find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

# Example Test case
num1, num2 = 48, 18
print(gcd(num1, num2))  

# Write a Python program to implement a basic version of the Collatz conjecture.

def collatz_conjecture(number):
    sequence = []
    while number != 1:
        sequence.append(number)
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
    sequence.append(1)
    return sequence

# Example Test case
number = 13
print(collatz_conjecture(number))  
