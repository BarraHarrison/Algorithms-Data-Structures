# Recursion is a technique where a function calls itself until a base condition is met

# Factorial Calculation
# Algorithm used in Probability

def factorial_recursive(n_factorial):
    if n_factorial == 0 or n_factorial == 1:
        return 1
    return n_factorial * factorial_recursive(n_factorial - 1)

n_factorial = 5
result_factorial = factorial_recursive(n_factorial)
print("Factorial of", n_factorial, "is:", result_factorial)
# Factorial of 5 is: 120


# Fibonacci Sequence

def fibonacci_recursive(n_fibonacci):
    if n_fibonacci == 0:
        return 0
    elif n_fibonacci == 1:
        return 1
    return fibonacci_recursive(n_fibonacci - 1) + fibonacci_recursive(n_fibonacci - 2)

n_fibonacci = 6
result_fibonacci = fibonacci_recursive(n_fibonacci)
print("Fibonacci of", n_fibonacci, "is:", result_fibonacci)


# Tower of Hanoi
# Move n disks form Source to Destination using Auxiliary as a helper

def tower_of_hanoi(n_hanoi, source, auxiliary, destination):
    if n_hanoi == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return 
    tower_of_hanoi(n_hanoi - 1, source, destination, auxiliary)
    print(f"Move disk {n_hanoi} from {source} to {destination}")
    tower_of_hanoi(n_hanoi - 1, auxiliary, source, destination)

n_hanoi = 3
print("Tower of Hanoi Moves:")
tower_of_hanoi(n_hanoi, "A", "B", "C")



# Divide & Conquer breaks the problem down into smaller subproblems

# Merge Sort
# Splits the list into halves, solves recursively and merges

def merge_sort_recursive(arr_merge_rec):
    if len(arr_merge_rec) > 1:
        mid = len(arr_merge_rec) // 2
        left_half = arr_merge_rec[:mid]
        right_half = arr_merge_rec[mid:]

        merge_sort_recursive(left_half)
        merge_sort_recursive(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr_merge_rec[k] = left_half[i]
                i += 1
            else:
                arr_merge_rec[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr_merge_rec[k] = left_half[i]
            i += 1
            j += 1

        while j < len(right_half):
            arr_merge_rec[k] = right_half[j]
            j += 1
            k += 1

    return arr_merge_rec

arr_merge_rec = [12, 11, 13, 24, 37, 5, 6, 7]
sorted_merge_rec = merge_sort_recursive(arr_merge_rec)
print("Merge Sort (Recursive):", sorted_merge_rec)


# Quick Sort
# Good for large datasets

def quick_sort_recursive(arr_quick_rec):
    if len(arr_quick_rec)<= 1:
        return arr_quick_rec
    pivot = arr_quick_rec[len(arr_quick_rec) // 2]
    left = [x for x in arr_quick_rec if x < pivot]
    middle = [x for x in arr_quick_rec if x == pivot]
    right = [x for x in arr_quick_rec if x > pivot]
    return quick_sort_recursive(left) + middle + quick_sort_recursive(right)

arr_quick_rec = [33, 10, 55, 71, 29, 3]
sorted_quick_rec = quick_sort_recursive(arr_quick_rec)
print("Quick Sort (Recursive):", sorted_quick_rec)