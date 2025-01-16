class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    dummy = ListNode(0)
    current, carry = dummy, 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next

def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()


l1 = ListNode(7)
l1.next = ListNode(1)
l1.next.next = ListNode(6)
l2 = ListNode(5)
l2.next = ListNode(9)
l2.next.next = ListNode(2)

result = add_two_numbers(l1, l2)
print_linked_list(result)