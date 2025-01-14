def invert_dict(dict):
    return {value: key for key, value in dict.items()}

dict = {'a': 1, 'b': 2, 'c': 3}
result = invert_dict(dict)
print(f"Input: {dict}")
print(f"Expected Output: {result}")