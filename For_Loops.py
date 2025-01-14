# Generate the Fibonacci series up to a given number of terms
def generate_fibonacci(terms):
    fib = [0, 1]
    for i in range(2, terms):
        fib.append(fib[-1] + fib[-2])
    return fib[:terms]

print(generate_fibonacci(7))  

# Find the longest increasing subsequence in a given list of numbers
def longest_increasing_subsequence(lst):
    n = len(lst)
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if lst[i] > lst[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    max_length = max(lis)
    subsequence = []
    for i in range(n - 1, -1, -1):
        if lis[i] == max_length:
            subsequence.append(lst[i])
            max_length -= 1
    return subsequence[::-1]


print(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]))  

