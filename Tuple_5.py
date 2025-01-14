# Merge two sorted tuples into one sorted tuple
def merge_sorted_tuples(tuple1, tuple2):
    return tuple(sorted(tuple1 + tuple2))

print(merge_sorted_tuples((1, 3, 5), (2, 4, 6)))  


# Find all unique combinations of elements in a tuple that sum up to a given number
from itertools import combinations

def combinations_with_sum(tup, target):
    result = []
    for r in range(1, len(tup) + 1):
        for combo in combinations(tup, r):
            if sum(combo) == target:
                result.append(combo)
    return result

print(combinations_with_sum((2, 3, 4, 5, 7), 11))  

