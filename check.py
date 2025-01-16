class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_last(self, data):
        node1 = Node(data)
        if self.head is None:
            self.head = node1
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node1  # Link the new node to the last node.

    def detect_loop(self):
        slow = self.head
        fast = self.head
        
        # Move fast pointer two steps and slow pointer one step
        while fast and fast.next:
            slow = slow.next          # Move slow pointer one step
            fast = fast.next.next     # Move fast pointer two steps
            
            if slow == fast:  # If the pointers meet, a loop is detected
                return True
        return False  # If we finish traversing without meeting, no loop is found

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
    ll.insert_at_last(1)
    ll.insert_at_last(2)
    ll.insert_at_last(3)
    ll.insert_at_last(4)
    
    # Printing the list to verify that the list is created correctly
    ll.printing()  # Output should be 1->2->3->4->

    # Now let's detect if there is a loop in the list
    if ll.detect_loop():
        print("Loop detected in the Linked List")
    else:
        print("No loop detected")
