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