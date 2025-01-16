# 1. Find the Minimum Element in a Stack
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            return self.stack.pop()

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None

s = MinStack()
s.push(3)
s.push(5)
s.push(2)
s.pop()
print(s.get_min())

# 2. Reverse a String Using a Stack
def reverse_string(s):
    stack = list(s)
    return ''.join(stack[::-1])

print(reverse_string("hello"))

# 3. Next Greater Element
def next_greater_element(arr):
    result = [-1] * len(arr)
    stack = []
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result

print(next_greater_element([4, 5, 2, 25]))

# 4. Implement a Stack Using Two Queues
from queue import Queue

class StackUsingQueues:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q1.put(x)

    def pop(self):
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        popped = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1
        return popped

    def top(self):
        return self.q1.queue[-1]

stack = StackUsingQueues()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())


# 5. Decode a String
def decode_string(s):
    stack = []
    curr_num = 0
    curr_str = ""
    for char in s:
        if char.isdigit():
            curr_num = curr_num * 10 + int(char)
        elif char == '[':
            stack.append((curr_str, curr_num))
            curr_str, curr_num = "", 0
        elif char == ']':
            prev_str, num = stack.pop()
            curr_str = prev_str + curr_str * num
        else:
            curr_str += char
    return curr_str

print(decode_string("3[a2[c]]"))
