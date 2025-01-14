def merge_and_sum_dicts(*dicts):
    result = {}
    for d in dicts:
        for key, value in d.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
    return result

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'a': 2, 'c': 1}

output = merge_and_sum_dicts(dict1, dict2, dict3)
print(f"Input: dict1 = {dict1}, dict2 = {dict2}, dict3 = {dict3}")
print(f"{output}")
