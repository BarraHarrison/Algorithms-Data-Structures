# Omega Notation
# Guarantees an algorithm will take a certain amount of time
# Basically the "best-case scenario" for each algorithm
# Eg. Searching through an unsorted list will take a certain amount of time

import time
import matplotlib.pyplot as plt 
import numpy as np 

def best_case_constant(n):
    return 1

def best_case_logarithmic(n):
    count = 0
    i = 1
    while i < n:
        i *= 2
        count += 1
    return count

def best_case_linear(n):
    return 1

def best_case_nlogn(n):
    count = 0
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
            count += 1
    return count

def best_case_quadratic(n):
    count = 0
    for i in range(n):
        for j in range(i):
            count += 1
    return count

def measure_time(func, n):
    start = time.time()
    func(n)
    return time.time() - start

input_sizes = np.array([2, 4, 8, 16, 32, 64, 128])

times = {
    "Ω(1)": [measure_time(best_case_constant, n) for n in input_sizes],
    "Ω(log n)": [measure_time(best_case_logarithmic, n) for n in input_sizes],
    "Ω(1) (Best Case Search)": [measure_time(best_case_linear, n) for n in input_sizes],
    "Ω(n log n)": [measure_time(best_case_nlogn, n) for n in input_sizes],
    "Ω(n^2)": [measure_time(best_case_quadratic, n) for n in input_sizes],
}

plt.figure(figsize=(10, 6))
for label, values in times.items():
    plt.plot(input_sizes, values, label=label, marker="o")

plt.yscale("log")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Omega (Ω) Complexity Growth - Best Case Scenarios")
plt.legend()
plt.grid(True)
plt.show()