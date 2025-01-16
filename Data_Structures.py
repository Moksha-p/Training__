# Arrays Solutions

# 1. Find the Second Largest Element in an Array
def second_largest(arr):
    unique_sorted = sorted(set(arr))
    return unique_sorted[-2] if len(unique_sorted) >= 2 else None

print(second_largest([1, 3, 4, 2]))  # Output: 3

# 2. Move All Zeroes to the End
def move_zeroes(arr):
    non_zeroes = [num for num in arr if num != 0]
    zeroes = [0] * (len(arr) - len(non_zeroes))
    return non_zeroes + zeroes

print(move_zeroes([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]

# 3. Find the Union and Intersection of Two Arrays
def union_intersection(arr1, arr2):
    union = list(set(arr1) | set(arr2))
    intersection = list(set(arr1) & set(arr2))
    return union, intersection

print(union_intersection([1, 2, 3], [2, 3, 4]))  # Output: ([1, 2, 3, 4], [2, 3])

# 4. Rotate an Array by K Steps
def rotate_array(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]

print(rotate_array([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]

# 5. Merge Intervals
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged

print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Output: [[1, 6], [8, 10], [15, 18]]


# Strings Solutions

# 1. Find the Frequency of Each Character
def char_frequency(s):
    from collections import Counter
    return dict(Counter(s))

print(char_frequency("apple"))  # Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}

# 2. Remove Duplicates from a String
def remove_duplicates(s):
    return "".join(sorted(set(s), key=s.index))

print(remove_duplicates("programming"))  # Output: "progamin"

# 3. Find the First Non-Repeating Character
def first_non_repeating(s):
    from collections import Counter
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

print(first_non_repeating("swiss"))  # Output: "w"

# 4. Check if a String is a Rotation of Another
def is_rotation(s1, s2):
    return len(s1) == len(s2) and s2 in s1 + s1

print(is_rotation("abcde", "cdeab"))  # Output: True

# 5. Compress a String Using the Counts of Repeated Characters
def compress_string(s):
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(f"{s[i - 1]}{count}")
            count = 1
    compressed.append(f"{s[-1]}{count}")
    return "".join(compressed)

print(compress_string("aaabbc"))  # Output: "a3b2c1"


# Queues Solutions

# 1. Implement a Queue Using Lists
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def display(self):
        return self.queue

    def is_empty(self):
        return len(self.queue) == 0

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.display())  # Output: [1, 2, 3]
print(q.dequeue())  # Output: 1
print(q.display())  # Output: [2, 3]

# 2. Check for a Palindrome Using a Queue
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))  # Output: True

# 3. Implement a Circular Queue
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            return "Queue is full"
        elif self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        elif self.front == self.rear:
            result = self.queue[self.front]
            self.front = self.rear = -1
            return result
        else:
            result = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return result

    def display(self):
        if self.is_empty():
            return []
        if self.rear >= self.front:
            return self.queue[self.front : self.rear + 1]
        else:
            return self.queue[self.front :] + self.queue[: self.rear + 1]

    def is_empty(self):
        return self.front == -1

cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print(cq.display())  # Output: [1, 2, 3]
print(cq.dequeue())  # Output: 1
print(cq.display())  # Output: [2, 3]

# 4. Sort a Queue
def sort_queue(q):
    return sorted(q)

print(sort_queue([3, 1, 4, 2]))  # Output: [1, 2, 3, 4]

# 5. Implement an LRU Cache
class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.order = []

    def get(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) == self.capacity:
            oldest = self.order.pop(0)
            del self.cache[oldest]
        self.cache[key] = value
        self.order.append(key)

lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  # Output: 1
lru.put(3, 3)
print(lru.get(2))  # Output: -1


# Stack Solutions

# 1. Find the Minimum Element in a Stack
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack:
            if self.stack.pop() == self.min_stack[-1]:
                self.min_stack.pop()

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None

ms = MinStack()
ms.push(3)
ms.push(5)
ms.push(2)
print(ms.get_min())  # Output: 2
ms.pop()
print(ms.get_min())  # Output: 3

# 2. Reverse a String Using a Stack
def reverse_string(s):
    stack = list(s)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str

print(reverse_string("hello"))  # Output: "olleh"

# 3. Next Greater Element
def next_greater_element(arr):
    result = [-1] * len(arr)
    stack = []
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result

print(next_greater_element([4, 5, 2, 25]))  # Output: [5, 25, 25, -1]

# 4. Implement a Stack Using Two Queues
from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        self.queue1.append(x)

    def pop(self):
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        result = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return result

    def top(self):
        return self.queue1[-1] if self.queue1 else None

stack_q = StackUsingQueues()
stack_q.push(1)
stack_q.push(2)
stack_q.push(3)
print(stack_q.pop())  # Output: 3

# 5. Decode a String
def decode_string(s):
    stack = []
    current_num = 0
    current_str = ""
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str, current_num = "", 0
        elif char == ']':
            last_str, num = stack.pop()
            current_str = last_str + current_str * num
        else:
            current_str += char
    return current_str

print(decode_string("3[a2[c]]"))  # Output: "accaccacc"


# Linked List Solutions

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# 1. Detect a Loop in a Linked List
def detect_loop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# 2. Remove Duplicates from a Sorted Linked List
def remove_duplicates(head):
    current = head
    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    return head

# 3. Check if a Linked List is a Palindrome
def is_palindrome_linked_list(head):
    vals = []
    current = head
    while current:
        vals.append(current.value)
        current = current.next
    return vals == vals[::-1]

# 4. Rotate a Linked List
def rotate_linked_list(head, k):
    if not head or k == 0:
        return head

    length = 1
    current = head
    while current.next:
        current = current.next
        length += 1

    k %= length
    if k == 0:
        return head

    current.next = head
    for _ in range(length - k):
        current = current.next
    new_head = current.next
    current.next = None
    return new_head

# 5. Add Two Numbers Represented by Linked Lists
def add_two_numbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.value if l1 else 0
        val2 = l2.value if l2 else 0
        total = val1 + val2 + carry
        carry, value = divmod(total, 10)
        current.next = ListNode(value)
        current = current.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy.next
