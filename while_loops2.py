def collatz(number):
    sequence = [number]
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        sequence.append(number)
    return sequence

print(collatz(13))  # Output: [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
