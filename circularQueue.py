class CircularQueue:
    def __init__(self, size):
        self.maxSize = size
        self.queueArray = [0] * size
        self.front = -1
        self.rear = -1
    
    def enqueue(self, item):
        if (self.front == 0 and self.rear == self.maxSize - 1) or (self.rear == (self.front - 1) % (self.maxSize - 1)):
            print("Queue is full")
            return
        elif self.front == -1:  
            self.front = self.rear = 0
        elif self.rear == self.maxSize - 1 and self.front != 0:  
            self.rear = 0
        else:  
            self.rear += 1
        self.queueArray[self.rear] = item

    def dequeue(self):
        if self.front == -1:  
            print("Queue is empty")
            return -1
        ans = self.queueArray[self.front]
        self.queueArray[self.front] = -1  

        if self.front == self.rear:  
            self.front = self.rear = -1
        elif self.front == self.maxSize - 1: 
            self.front = 0
        else:  
            self.front += 1
        
        return ans

    def peek(self):
        if not self.isEmpty():
            return self.queueArray[self.front]
        else:
            print("Queue is empty.")
            return -1

    def isEmpty(self):
        return self.front == -1

if __name__ == '__main__':
    q = CircularQueue(5)  
    q.enqueue(5)
    print(q.peek())  
    q.enqueue(10)
    print(q.dequeue()) 
    print(q.peek()) 
