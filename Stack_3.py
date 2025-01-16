def next_greater_element(arr):
    stack, result = [], [-1] * len(arr)
    for i, num in enumerate(arr):
        while stack and arr[stack[-1]] < num:
            result[stack.pop()] = num
        stack.append(i)
    return result

print(next_greater_element([4, 5, 2, 25]))  # Output: [5, 25, 25, -1]