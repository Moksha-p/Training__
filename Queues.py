# 1. Implement a Queue Using Lists
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        return self.queue.pop(0) if self.queue else None
    
    def display(self):
        return self.queue

q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
print(q.display())

# 2. Check for a Palindrome Using a Queue
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))

# 3. Implement a Circular Queue
class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
            return None
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def display(self):
        if self.front == -1:
            return []
        elif self.rear >= self.front:
            return self.queue[self.front:self.rear + 1]
        else:
            return self.queue[self.front:] + self.queue[:self.rear + 1]

cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.dequeue()
print(cq.display())


# 4. Sort a Queue
from queue import Queue

def sort_queue(q):
    lst = []
    while not q.empty():
        lst.append(q.get())
    lst.sort()
    for item in lst:
        q.put(item)
    return list(q.queue)

q = Queue()
for item in [3, 1, 4, 2]:
    q.put(item)

print(sort_queue(q))


# 5. Implement an LRU Cache
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

    def display(self):
        return list(self.cache.items())

lru = LRUCache(3)
lru.put(1, 1)
lru.put(2, 2)
lru.put(3, 3)
lru.put(4, 4)
print(lru.get(2))
print(lru.display())
