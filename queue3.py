class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            return "Queue is full"
        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            return "Queue is empty"
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return item

    def display(self):
        if self.front == -1:
            return []
        if self.rear >= self.front:
            return self.queue[self.front:self.rear+1]
        return self.queue[self.front:] + self.queue[:self.rear+1]

q = CircularQueue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.display())
q.dequeue()
print(q.display())
