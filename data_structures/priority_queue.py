# Priority-Queue: Type of Queue where elements are removed based on priority instead of arrival order
# Basically the element with highest priority is removed first
# heapq module provides lowest-value highest-priority

import heapq

priority_queue = []

heapq.heappush(priority_queue, (3, "Task C"))
heapq.heappush(priority_queue, (1, "Task A"))
heapq.heappush(priority_queue, (2, "Task B"))

print("Priority Queue:", priority_queue)

print("Dequeued:", heapq.heappop(priority_queue))
print("Priority Queue after pop:", priority_queue)