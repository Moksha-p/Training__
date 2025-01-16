def reverse_string(s):
    stack = list(s)
    return ''.join([stack.pop() for _ in range(len(stack))])

print(reverse_string("hello"))  