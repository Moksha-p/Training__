def rotate_array(arr, k):
    k = k % len(arr) # as to handle the case when the k > len(arr) 
    return arr[-k:] + arr[:-k]

print(rotate_array([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]
