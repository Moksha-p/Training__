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
q.enqueue(3)
print(q.display())
q.dequeue()
print(q.display())
