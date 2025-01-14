# Create a function to merge two sorted tuples into one sorted tuple.

def merge_tuples(tuple1, tuple2):
    
    return tuple(sorted(tuple1 + tuple2))

# Example Test Case
tuple1 = (1, 3, 5)
tuple2 = (2, 4, 6)
result = merge_tuples(tuple1, tuple2)
print(result)  


# Write a Python program to find all unique combinations of elements in a tuple that sum up to a given number.

from itertools import combinations

def find_combinations_that_sum_to_target(tup, target):
    result = []

    for i in range(1, len(tup) + 1):
        for comb in combinations(tup, i):
            if sum(comb) == target:
                result.append(comb)
    return result

# Example Test Case
tuple = (2, 3, 5, 7)
target = 10
result = find_combinations_that_sum_to_target(tuple, target)
print(result)  
