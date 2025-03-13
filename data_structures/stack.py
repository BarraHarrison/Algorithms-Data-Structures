# Stack: Linear Data Structure that follows the LIFO principle
# Stack-Overflow: When a stack exceeds its memory limit
# Implementing a stack using the collections.deque module

from collections import deque

stack = deque()

stack.append("A")
stack.append("B")
stack.append("C")

print("Stack after pushes:", stack)

print("Popped:", stack.pop())
print("Stack after pop:", stack)