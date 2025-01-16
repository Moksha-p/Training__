class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self,data):
        node1 = Node(data)
        node1.next = self.head
        self.head  = node1

    def insert_at_last(self , data):
        node1 = Node(data)
        if self.head is None:
            self.head = node1
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next  = node1
    
    def insert_at_position (self, position , data):
        if(position == 1):
            ll.insert_at_head(data)
            return
        
        temp = self.head
        count = 1
        while count < (position - 1):
            temp = temp.next
            count += 1
        if temp.next == None:
            ll.insert_at_last(data)
            return
        node1 = Node(data)
        node1.next = temp.next
        temp.next = node1

    def reverseLL(self):
        if self.head is None or self.head.next is None:
            return 

        
        prev = None
        curr = self.head
        forward = None
        while(curr != None):
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
        self.head = prev
        

    def detect_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
            if slow == fast:
                return True
        return False
    

    def removeDup(self):
        if self.head is None:
            return None
        curr = self.head
        while curr != None:
            if curr.next is not None and curr.data is curr.next.data:
                curr.next = curr.next.next
                
                
                
            else:
                curr = curr.next

    def isPalindrome(self):
        arr = []
        temp = self.head
        while temp != None:
            arr.append(temp.data)
            temp = temp.next
        return arr == arr[::-1] 
        


    def rotateLL(self , k):
        if k == 0 or self.head is None or self.head.next is None:
            return
        length = 1
        tail = self.head
        while tail.next:
            tail = tail.next
            length += 1
        k = k % length
        if k == 0:
            return 
        new_tail_p = length - k - 1
        new_tail = self.head
        for i in range(new_tail_p):
            new_tail = new_tail.next
        new_head = new_tail.next

        new_tail.next = None
        tail.next = self.head 
        self.head = new_head

    def printing(self):
        if self.head is None:
            print("Empty")
            return
       
        itr = self.head
        liStr = ''
        while itr:
            liStr += str(itr.data) + '->'
            itr = itr.next
        print(liStr)

if __name__ == '__main__':
    ll = LinkedList()

    ll.insert_at_head(5)
    ll.insert_at_head(10)
    ll.insert_at_head(15)
    ll.insert_at_last(55)
    ll.insert_at_position(1,20)
    ll.insert_at_position(2,25)
    ll.insert_at_position(6,50)
    ll.insert_at_position(8,100)
    ll.printing()
    print("Reverse " , ll.reverseLL())
    ll.printing()
 
    
   
    ll.printing()
    ll.insert_at_last(1)
    ll.insert_at_last(2)
    ll.insert_at_last(2)
    ll.insert_at_last(3)
    ll.insert_at_last(3)
    ll.insert_at_last(4)
    ll.insert_at_last(4)
    ll.insert_at_head(10)
    ll.removeDup()
 
ll.insert_at_last(1)
ll.insert_at_last(2)
ll.insert_at_last(2)
ll.insert_at_last(1)
k=2
ll.rotateLL(k)
ll.printing()
print("Palindrome? : ",ll.isPalindrome())
ll.printing()
     
if ll.detect_loop():
    print("True")
else:
    print("False")





