from numpy import sort


class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,element):
        self.queue.append(element) 
        print(element)
    def dequeue(self ):
        if self.is_empty():
            print("Empty")
            return None
        return self.queue.pop(0)
    def display(self):
        if self.is_empty():
            print("Empty")
        else:
            print("Content: " , self.queue)


    def is_empty(self):
        return len(self.queue) == 0   

    def isPalindrome(self):
        return self.queue == self.queue[::-1]
    def sorting(self):
        return sort(self.queue)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(30)
    q.enqueue(20)
    q.enqueue(30)
    #q.enqueue("radar")
    q.display()
    q.isPalindrome()
    q.display()
    q.sorting()

    if q.isPalindrome():
        print("palindrome.")
    else:
        print("not palindrome.")
    
