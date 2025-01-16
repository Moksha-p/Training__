#Arrays
#Find the Second Largest Element in an Array
def second_largest(arr):
    arr = list(set(arr))  # Remove duplicates
    arr.sort()
    return arr[-2] if len(arr) >= 2 else None

# Example usage
print(second_largest([1, 3, 4, 2]))  # Output: 3


#Move All Zeroes to the End
def move_zeroes(arr):
    non_zero_elements = [num for num in arr if num != 0]
    zero_elements = [0] * (len(arr) - len(non_zero_elements))
    return non_zero_elements + zero_elements

# Example usage
print(move_zeroes([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]


#Find the Union and Intersection of Two Arrays

def union_intersection(arr1, arr2):
    union = list(set(arr1).union(set(arr2)))
    intersection = list(set(arr1).intersection(set(arr2)))
    return union, intersection

# Example usage
arr1 = [1, 2, 3]
arr2 = [2, 3, 4]
union, intersection = union_intersection(arr1, arr2)
print(f"Union: {union}, Intersection: {intersection}")
# Output: Union: [1, 2, 3, 4], Intersection: [2, 3]


#Rotate an Array by K Steps
def rotate_array(arr, k):
    k = k % len(arr)  # Handle cases where k > len(arr)
    return arr[-k:] + arr[:-k]

# Example usage
print(rotate_array([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]



#Merge Intervals

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])  # Sort by the start value of intervals
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # Overlapping intervals
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged

# Example usage
print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Output: [[1, 6], [8, 10], [15, 18]]


#Strings

#Find the Frequency of Each Character
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Example usage
print(char_frequency("apple"))  # Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}


#Remove Duplicates from a String
def remove_duplicates(s):
    return "".join(sorted(set(s), key=s.index))

# Example usage
print(remove_duplicates("programming"))  # Output: "progamin"

#Find the First Non-Repeating Character
def first_non_repeating(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

# Example usage
print(first_non_repeating("swiss"))  # Output: "w"

#Check if a String is a Rotation of Another
def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    return str2 in str1 + str1

# Example usage
print(is_rotation("abcde", "cdeab"))  # Output: True

#Compress a String Using the Counts of Repeated Characters
def compress_string(s):
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed.append(s[i-1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))  # Append the last character
    return "".join(compressed)

# Example usage
print(compress_string("aaabbc"))  # Output: "a3b2c1"


#Queues

#Implement a Queue Using Lists

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):

        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"

    def display(self):

        return self.queue

    def is_empty(self):
        return len(self.queue) == 0

# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.display())  # Output: [10, 20, 30]
print(q.dequeue())  # Output: 10
print(q.display())  # Output: [20, 30]

#Check for a Palindrome Using a Queue

from collections import deque

def is_palindrome(s):
    queue = deque(s)  # Using deque for efficient pops from both ends
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True

# Example usage
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False


#Implement a Circular Queue

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            return "Queue is Full"
        elif self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            return "Queue is Empty"
        value = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return value

    def display(self):
        if self.front == -1:
            return "Queue is Empty"
        result = []
        i = self.front
        while True:
            result.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        return result

# Example usage
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
print(cq.display())  # Output: [10, 20, 30]
print(cq.dequeue())  # Output: 10
print(cq.display())  # Output: [20, 30]


#Sort a Queue

from collections import deque

def sort_queue(q):
    size = len(q)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if q[j] < q[min_index]:
                min_index = j
        # Rotate the queue to bring the smallest element to the front
        for _ in range(min_index):
            q.append(q.popleft())
    return list(q)

# Example usage
q = deque([3, 1, 4, 2])
sorted_queue = sort_queue(q)
print(sorted_queue)  # Output: [1, 2, 3, 4]


#Implement an LRU Cache

from collections import deque

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = deque()

    def get(self, key):
        if key in self.cache:
            # Move the accessed item to the end (most recently used)
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            # Remove the old key and update its position
            self.order.remove(key)
        elif len(self.cache) == self.capacity:
            # Remove the least recently used key (front of the queue)
            lru = self.order.popleft()
            del self.cache[lru]
        # Add the new key-value pair to the cache and update its position
        self.cache[key] = value
        self.order.append(key)

    def display(self):
        return self.cache

# Example usage
lru_cache = LRUCache(2)
lru_cache.put(1, 10)
lru_cache.put(2, 20)
print(lru_cache.display())  # Output: {1: 10, 2: 20}
print(lru_cache.get(1))  # Output: 10
lru_cache.put(3, 30)
print(lru_cache.display())  # Output: {1: 10, 3: 30} (2 is evicted)


#Stack Problems

#Find the Minimum Element in a Stack

class SpecialStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Stack to keep track of the minimum value

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if self.stack:
            value = self.stack.pop()
            if value == self.min_stack[-1]:
                self.min_stack.pop()
            return value
        return None

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None

# Example usage
s = SpecialStack()
s.push(10)
s.push(5)
s.push(20)
print(s.get_min())  # Output: 5
s.pop()
print(s.get_min())  # Output: 5


#Reverse a String Using a Stack

def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_str = ''.join([stack.pop() for _ in range(len(stack))])
    return reversed_str

#Next Greater Element

def next_greater_element(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)

    return result

#Implement a Stack Using Two Queues
from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, value):
        self.queue1.append(value)

    def pop(self):
        if not self.queue1:
            return None
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        value = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1  # Swap the queues
        return value

    def top(self):
        if self.queue1:
            return self.queue1[-1]
        return None

# Example usage
stack = StackUsingQueues()
stack.push(10)
stack.push(20)
print(stack.pop())  # Output: 20
print(stack.top())  # Output: 10

#Decode a String
def decode_string(s):
    stack = []
    current_num = 0
    current_str = ""

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)  # Handling multi-digit numbers
        elif char == '[':
            stack.append((current_num, current_str))
            current_num = 0
            current_str = ""
        elif char == ']':
            num, prev_str = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char

    return current_str


# Example usage
print(decode_string("3[a2[c]]"))  # Output: "accaccacc"


#Linked List Problems
#Detect a Loop in a Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detect_loop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Example usage
# 1 -> 2 -> 3 -> 4 -> 2 (loop)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creates a loop

print(detect_loop(node1))  # Output: True

#Remove Duplicates from a Sorted Linked List
def remove_duplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

# Example usage
node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

new_head = remove_duplicates(node1)
while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next  # Output: 1 -> 2 -> 3 ->


#Check if a Linked List is a Palindrome
def is_palindrome(head):
    # Step 1: Find the middle of the linked list
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    # Step 3: Compare the first and second halves
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


# Example usage
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(is_palindrome(node1))  # Output: True


#Rotate a Linked List

def rotate_linked_list(head, k):
    if not head or k == 0:
        return head

    # Step 1: Find the length of the linked list
    length = 1
    tail = head
    while tail.next:
        length += 1
        tail = tail.next

    # Step 2: Find the new head after rotation
    k = k % length
    if k == 0:
        return head

    # Step 3: Rotate the list
    current = head
    for _ in range(length - k - 1):
        current = current.next
    new_head = current.next
    current.next = None
    tail.next = head

    return new_head


# Example usage
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

new_head = rotate_linked_list(node1, 2)
while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next  # Output: 4 -> 5 -> 1 -> 2 -> 3 ->

#Add Two Numbers Represented by Linked Lists

def add_two_numbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next


# Example usage
node1 = ListNode(7)
node2 = ListNode(1)
node3 = ListNode(6)
node1.next = node2
node2.next = node3  # 617

node4 = ListNode(5)
node5 = ListNode(9)
node6 = ListNode(2)
node4.next = node5
node5.next = node6  # 295

result = add_two_numbers(node1, node4)
while result:
    print(result.val, end=" -> ")
    result = result.next  # Output: 2 -> 1 -> 9 ->




