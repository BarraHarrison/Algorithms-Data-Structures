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


# Binary Search
# Split the list in half and check whether to go left or right

def binary_search_iterative(arr_one, target_one):
    left, right = 0, len(arr_one) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr_one[mid] == target_one:
            return mid
        elif arr_one[mid] < target_one:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr_one = [10, 20, 30, 40, 50, 60, 70, 80]
target_one = 40
result = binary_search_iterative(arr_one, target_one)
print("Target not found at index:", result) if result != -1 else print("Target not found")