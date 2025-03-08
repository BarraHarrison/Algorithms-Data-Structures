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
    pass