input = [1, 2, 3, 4, 5]
k = 2

n = len(input)
k = k % n
print(input[-k:] + input[:-k])    