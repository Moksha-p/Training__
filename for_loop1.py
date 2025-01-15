def fibonacci(terms):
    series = [0, 1]
    while len(series) < terms:
        series.append(series[-1] + series[-2])
    return series[:terms]

print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]
