def move_zeroes(arr):
    non_zeroes = [x for x in arr if x != 0]
    zeroes = [0] * (len(arr) - len(non_zeroes))
    return non_zeroes + zeroes

print(move_zeroes([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]
