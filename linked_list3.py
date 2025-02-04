class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    # Find the midpoint
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # Reverse the second half of the list
    prev, current = None, slow
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    # Compare the first half with the reversed second half
    first, second = head, prev
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    return True

# Example: 1 -> 2 -> 3 -> 2 -> 1
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
print(is_palindrome(head))  # Output: True
