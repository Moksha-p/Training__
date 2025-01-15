import itertools

def generate_permutations(lst):
    return list(itertools.permutations(lst))

print(generate_permutations([1, 2, 3]))  # Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
