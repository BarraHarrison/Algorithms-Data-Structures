# Dynamic Programming Algorithms
# Breaks down problems into subproblems
# Solves them using memoization (top-down) or tabulation (bottom-up)

# Fibonacci Sequence
# Optimized with Memoization

def fibonacci_dp_memo(n_fibonacci, memo_fibonacci={}):
    if n_fibonacci in memo_fibonacci:
        return memo_fibonacci[n_fibonacci]
    if n_fibonacci <= 0:
        return 0
    elif n_fibonacci == 1:
        return 1
    memo_fibonacci[n_fibonacci] = fibonacci_dp_memo(n_fibonacci - 1, memo_fibonacci) + fibonacci_dp_memo(n_fibonacci - 2, memo_fibonacci)
    return memo_fibonacci[n_fibonacci]

n_fibonacci = 10
result_fibonacci = fibonacci_dp_memo(n_fibonacci)
print("Fibonacci (DP Memoization):", result_fibonacci)


# Fibonacci Sequence
# Optimized with Tabulation

def tabulation_fibonacci(x_fibonacci):
    if x_fibonacci <= 0:
        return 0
    elif x_fibonacci == 1:
        return 1
    
    fib_table = [0] * (x_fibonacci + 1)
    fib_table[1] = 1

    for i in range(2, x_fibonacci + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]

    return fib_table[x_fibonacci]

x_fibonacci = 10
result_tabulation_fibonacci = tabulation_fibonacci(x_fibonacci)
print("Fibonacci (DP Tabulation):", result_tabulation_fibonacci)