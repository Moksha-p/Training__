# Find the symmetric difference between two sets
def symmetric_difference(set1, set2):
    return set1 ^ set2

print(symmetric_difference({1, 2, 3}, {3, 4, 5}))  

from itertools import combinations
# Find all subsets of a given set
def all_subsets(s):
    result = []
    for r in range(len(s) + 1):
        for subset in combinations(s, r):
            result.append(set(subset))
    return result

print(all_subsets({1, 2, 3}))  
