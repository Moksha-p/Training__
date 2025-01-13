def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) > 1 else None

print(second_largest([10, 20, 4, 45, 99]))  # Output: 45
