# Big-O Notation
# A mathematical way of looking at which function is limiting another function
import time
import matplotlib.pyplot as plt 
import numpy as np 

def constant_time(n):
    return 1

def logarithmic_time(n):
    count = 0
    while n < 1:
        n //= 2
        count += 1
    return count

def linear_time(n):
    count = 0
    for _ in range(n):
        j = 1
        while j < n:
            j *= 2
            count += 1
    return count

def nlogn_time(n):
    # O(n log n) - Common in sorting algorithms like Merge Sort
    count = 0
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
            count += 1
    return count

def quadratic_time(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

def exponential_time(n):
    if n == 0:
        return 1
    return 2 * exponential_time(n - 1)
    # O(2^n) - Recursive exponential growth

def measure_time(func, n):
    start = time.time()
    func(n)
    return time.time() - start

input_sizes = np.array([2, 4, 8, 16, 32, 64, 128])

# Measure time of each function
times = {
    "0(1)": [measure_time(constant_time, n) for n in input_sizes],
    "0(log n)": [measure_time(logarithmic_time, n) for n in input_sizes],
    "0(n)": [measure_time(linear_time, n) for n in input_sizes],
    "0(n log n)": [measure_time(nlogn_time, n) for n in input_sizes],
    "0(n^2)": [measure_time(quadratic_time, n) for n in input_sizes],
    "0(2^n)": [measure_time(exponential_time, n) for n in input_sizes if n <= 20],
}

# The graph shows how different algorithms grow as input size (n) increases
plt.figure(figsize=(10, 6))
for label, values in times.items():
    plt.plot(input_sizes[:len(values)], values, label=label, marker="o")

plt.yscale("log")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Big-O Complexity Growth")
plt.legend
plt.grid(True)
plt.show()