# Searching Algorithms

# Linear Search
# Iterates through a list to find an element

def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

array = [10, 20, 30, 40, 50]
target = 40
result = linear_search(array, target)
print("Target found at index:", result) if result != -1 else print("Target not found")