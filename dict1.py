def invert_dictionary(d):
    return {v: k for k, v in d.items()}

print(invert_dictionary({'a': 1, 'b': 2, 'c': 3}))  # Output: {1: 'a', 2: 'b', 3: 'c'}
