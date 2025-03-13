# Queue: Linear Data Structure but follows the FIFO principle
# Similar to Stacks but it adds and removes elements in a different way

from collections import deque

queue = deque()

queue.append("A")
queue.append("B")
queue.append("C")

print("Queue after enqueue:", queue)
print("Dequeued:", queue.popleft())
print("Queue after dequeue:", queue)

# Queue after enqueue: deque(['A', 'B', 'C'])
# Dequeued: A
# Queue after dequeue: deque(['B', 'C'])