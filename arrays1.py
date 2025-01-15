def second_largest(arr):
    arr = list(set(arr))
    arr.sort()  
    return arr[-2] if len(arr) >= 2 else None

print(second_largest([1, 3, 4, 2]))  # Output: 3
