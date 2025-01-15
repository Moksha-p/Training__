def union_intersection(arr1, arr2):
    union = list(set(arr1) | set(arr2))
    intersection = list(set(arr1) & set(arr2))
    return union, intersection

arr1 = [1, 2, 3]
arr2 = [2, 3, 4]
print(union_intersection(arr1, arr2))
