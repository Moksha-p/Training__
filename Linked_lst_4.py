class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotate_linked_list(head, k):
    if not head or not head.next:
        return head

    length, tail = 1, head
    while tail.next:
        length += 1
        tail = tail.next

    k = k % length
    if k == 0:
        return head
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    tail.next = head
    return new_head

def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

head = rotate_linked_list(head, 2)

print_linked_list(head)