from collections import Counter

def merge_and_sum_dicts(*dicts):
    return dict(sum((Counter(d) for d in dicts), Counter()))

print(merge_and_sum_dicts({'a': 1, 'b': 2, 'c': 4}, {'b': 3, 'c': 4}))  # Output: {'a': 1, 'b': 5, 'c': 4}
