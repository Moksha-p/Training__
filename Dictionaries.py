# Write a Python function to invert a dictionary, swapping keys and values.

def invert_dict(d):
    
    return {v: k for k, v in d.items()}

# Example Test Case
input_dict = {'a': 1, 'b': 2, 'c': 3}
output_dict = invert_dict(input_dict)
print(output_dict)


# Write a Python program to merge multiple dictionaries and sum the values of common keys.

def merge_and_sum_dicts(*dicts):
    result = {}
    for d in dicts:
        for key, value in d.items():
            if key in result:
                result[key] += value  
            else:
                result[key] = value
    return result

# Example Test Case
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'b': 5, 'c': 4}
output_dict = merge_and_sum_dicts(dict1, dict2)
print(output_dict)
