class Node:
    def __init__(self,val = 0,next=None):
        self.val = val
        self.next = next

def remov(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

def display(Node):
    while Node:
        print(Node.val, end=" -> " if Node.next else "")
        Node = Node.next
    print()

head = Node(1)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(3)


head = remov(head)
display(head)









