from queue import Queue

def sort_queue(q):
    temp_stack = []
    while not q.empty():
        temp = q.get()
        while temp_stack and temp_stack[-1] > temp:
            q.put(temp_stack.pop())
        temp_stack.append(temp)
    while temp_stack:
        q.put(temp_stack.pop(0))
    return q

q = Queue()
for item in [3, 1, 4, 2]:
    q.put(item)
sorted_q = sort_queue(q)
sorted_list = []
while not sorted_q.empty():
    sorted_list.append(sorted_q.get())
print(sorted_list)