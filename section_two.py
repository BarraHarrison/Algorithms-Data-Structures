# Sorting Algorithms

# Bubble Sort Algorithm
# Comparing adjacent elements and swapping them if needed

def bubble_sort(arr_bubble):
    n = len(arr_bubble)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr_bubble[j] > arr_bubble[j+1]:
                arr_bubble[j], arr_bubble[j+1] = arr_bubble[j+1], arr_bubble[j]
        return arr_bubble
    
arr_bubble = [64, 25, 12, 22, 11, 47]
sorted_bubble = bubble_sort(arr_bubble)
print("Bubble Sort:", sorted_bubble)



# Selection Sorting Algorithm
# Find the smartest element and place it in the correct position

def selection_sort(arr_selection):
    n = len(arr_selection)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr_selection[j] < arr_selection[min_index]:
                min_index = j
        arr_selection[i], arr_selection[min_index] = arr_selection[min_index], arr_selection[i]
    return arr_selection

arr_selection = [29, 10, 14, 37, 13, 55, 7, 48]
sorted_selection = selection_sort(arr_selection)
print("Selection Sorted:", sorted_selection)


# Merge Sort Algorithm
# Recursively split the list into halves then sort and merge

def merge_sort(arr_merge):
    if len(arr_merge) > 1:
        mid = len(arr_merge) // 2
        left_half = arr_merge[:mid]
        right_half = arr_merge[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr_merge[k] = left_half[i]
                i += 1
            else:
                arr_merge[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr_merge[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr_merge[k] = right_half[j]
            j += 1
            k += 1
    return arr_merge

arr_merge = [38, 27, 43, 3, 9, 82, 10]
sorted_merge = merge_sort(arr_merge)
print("Merge Sort:", sorted_merge)

# Quick Sort Algorithm
# Start from a pivot, partition elements and recursively sort

def quick_sort(arr_quick):
    if len(arr_quick) <= 1:
        return arr_quick
    pivot = arr_quick[len(arr_quick) // 2]
    left = [x for x in arr_quick if x < pivot]
    middle = [x for x in arr_quick if x == pivot]
    right = [x for x in arr_quick if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr_quick = [33, 10, 55, 71, 29, 3]
sorted_quick = quick_sort(arr_quick)
print("Quick Sort:", sorted_quick)