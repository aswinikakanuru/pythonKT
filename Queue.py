'''Queue

A Queue is a data structure where the element that is added first is removed first.
FIFO = First In, First Out

'''
from collections import deque
queue=deque()
queue.append(10)
queue.append(20)
queue.append(30)

print(queue)
print(queue.popleft())
print(queue[0])
