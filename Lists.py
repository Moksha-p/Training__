# Write a Python function to find the second largest element in a list.

def second_largest(nums):
   
    nums = list(set(nums))
    nums.sort(reverse=True)
    return nums[1] if len(nums) > 1 else None 

# Example Test Case
nums = [10, 20, 4, 45, 99]
print("Second largest element:", second_largest(nums))


# Write a Python program to generate all possible permutations of a list of numbers.

import itertools

def generate_permutations(nums):
    return [list(perm) for perm in itertools.permutations(nums)]

# Example Test Case
nums = [1, 2, 3]
print("All permutations:", generate_permutations(nums))
