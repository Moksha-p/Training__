from collections import deque

def is_palindrome(s):
    queue = deque(s)
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True

print(is_palindrome("radar"))
print(is_palindrome("racecar"))