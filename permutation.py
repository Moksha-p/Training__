from itertools import permutations

def generate_permutations(numbers):
    return [list(p) for p in permutations(numbers)]

numbers = [1, 2, 3]

result = generate_permutations(numbers)
print(f"Input: {numbers}")
print(f"{result}")