# Find the second largest element in a list
def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2]

print(second_largest([10, 20, 4, 45, 99, 78, 89]))  


# Generate all possible permutations of a list of numbers
from itertools import permutations

def all_permutations(lst):
    return list(permutations(lst))

print(all_permutations([1, 2, 3]))  
