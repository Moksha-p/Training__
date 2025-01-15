from itertools import chain, combinations

def find_subsets(s):
    return [set(x) for x in chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))]

print(find_subsets({1, 2, 3}))  # Output: [set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
