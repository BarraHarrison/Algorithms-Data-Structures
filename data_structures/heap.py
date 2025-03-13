# Heap: Binary-Tree based data structure used to maintain priority-queues
# Min-Heap: Smallest value is at the root
# Max-Heap: Largest value is at the root

# Heapify-Up: New insert placed at the bottom of the tree, works its way "up"
# Heapify-Down: Replace the root with the last element
import random

class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify_up(self, index):
        """Heapify up is used when inserting a new element"""
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_up(parent)

    def heapify_down(self, index):
        """Heapify down is used when replacing the root with the last element"""
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

    def push(self, value):
        """Insert a value into the heap"""
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        """Remove and return the smallest value"""
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def peek(self):
        """Get the smallest value without removing it"""
        return self.heap[0] if self.heap else None

# Task Scheduling Example     
heap = MinHeap()
tasks = [
    "Process Data",
    "Train AI Model",
    "Send Email Notification",
    "Generate Report",
    "User Authentication",
    "Database Backup",
    "Optimize Images",
    "Monitor System Logs",
    "Run Scheduled Job",
    "Update Dashboard"
]

for task in tasks:
    priority = random.randint(1, 10)
    heap.push(priority, task)
    print(f"Added Task: {task} with Priority {priority}")

print("n\Priority Queue (Min-Heap):", heap.heap)

print("\nProcessing Tasks:")
while not heap.is_empty():
    priority, task = heap.pop()
    print(f"Processing Task: {task} (Priority {priority})")

print("n\All tasks completed!")