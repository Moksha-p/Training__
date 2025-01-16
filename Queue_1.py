class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,val):
        if val not in self.queue:
            self.queue.insert(0,val)
            return True
        return False
    
    def dequeue(self,val):
        if len(self.queue) > 0:
            self.queue.pop()
            return True
        return False

    
    def __repr__(self):
        return self.queue
    

q = Queue()
print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))

print(q)




