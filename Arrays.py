# 1 . Find the Second Largest Element in an Array
def second_largest(arr):
    unique = list(set(arr))
    unique.sort()
    return unique[-2] if len(unique) > 1 else None

print(second_largest([1, 3, 4, 2]))

# 2 . Move All Zeroes to the End
def move_zeroes(arr):
    return [x for x in arr if x != 0] + [x for x in arr if x == 0]

print(move_zeroes([0, 1, 0, 3, 12]))

# 3 . Find the Union and Intersection of Two Arrays
def union_intersection(arr1, arr2):
    union = list(set(arr1) | set(arr2))
    intersection = list(set(arr1) & set(arr2))
    return union, intersection

print(union_intersection([1, 2, 3], [2, 3, 4]))

# 4. Rotate an Array by K Steps
def rotate_array(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]

print(rotate_array([1, 2, 3, 4, 5], 2))

# 5. Merge Intervals
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))

