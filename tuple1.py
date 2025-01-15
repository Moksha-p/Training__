def merge_sorted_tuples(tuple1, tuple2):
    return tuple(sorted(tuple1 + tuple2))

print(merge_sorted_tuples((1, 3, 5), (2, 4, 6)))  # Output: (1, 2, 3, 4, 5, 6)
