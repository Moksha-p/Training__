# Write a Python program to find the symmetric difference between two sets.

def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

# Example Test Case
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Output
result = symmetric_difference(set1, set2)
print(result)


# Write a Python function to find all subsets of a given set.

from itertools import chain, combinations

def all_subsets(input_set):
    return [set(comb) for comb in chain.from_iterable(combinations(input_set, r) for r in range(len(input_set)+1))]

# Example Test Case
input_set = {1, 2, 3}

# Output
result = all_subsets(input_set)
print(result)
