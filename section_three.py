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