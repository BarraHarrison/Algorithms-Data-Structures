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

