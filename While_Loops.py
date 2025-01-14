
# Find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm
def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

print(gcd(48, 18))  

# Implement a basic version of the Collatz conjecture
def collatz_conjecture(number):
    result = []
    while number != 1:
        result.append(number)
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
    result.append(1)
    return result

print(collatz_conjecture(13)) 