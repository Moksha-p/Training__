# Invert a dictionary
def invert_dictionary(d):
    return {v: k for k, v in d.items()}

print(invert_dictionary({'a': 1, 'b': 2, 'c': 3, 'd': 4}))  

# Merge multiple dictionaries and sum the values of common keys
def merge_sum_dicts(*dicts):
    merged_dict = {}
    for d in dicts:
        for key, value in d.items():
            merged_dict[key] = merged_dict.get(key, 0) + value
    return merged_dict

print(merge_sum_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))  
