from queue import Queue

class StackUsingQueues:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x):
        self.queue1.put(x)

    def pop(self):
        if self.queue1.empty():
            return None
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        popped = self.queue1.get()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return popped

stack = StackUsingQueues()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
print(stack.pop())  # Output: 1