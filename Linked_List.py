# 1. Detect a Loop in a Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def detect_loop(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# 2. Remove Duplicates from a Sorted Linked List
def remove_duplicates(head):
    current = head
    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    return head

# 3. Check if a Linked List is a Palindrome
def is_palindrome(head):
    stack, slow, fast = [], head, head
    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next
    if fast:  # Odd number of elements
        slow = slow.next
    while slow:
        if stack.pop() != slow.value:
            return False
        slow = slow.next
    return True

# 4. Rotate a Linked List
def rotate_linked_list(head, k):
    if not head or k == 0:
        return head
    length, tail = 1, head
    while tail.next:
        tail = tail.next
        length += 1
    k %= length
    if k == 0:
        return head
    tail.next = head
    for _ in range(length - k):
        tail = tail.next
    new_head = tail.next
    tail.next = None
    return new_head

# 5. Add Two Numbers Represented by Linked Lists
def add_two_numbers(l1, l2):
    dummy = Node(0)
    current, carry = dummy, 0
    while l1 or l2 or carry:
        val1 = l1.value if l1 else 0
        val2 = l2.value if l2 else 0
        carry, out = divmod(val1 + val2 + carry, 10)
        current.next = Node(out)
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next

