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


# 0/1 Knapsack Problem
# Maximize the value without exceeding capacity

def knapsack_function(weights_knapsack, values_knapsack, capacity_knapsack):
    n = len(weights_knapsack)
    the_table = [[0] * (capacity_knapsack + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity_knapsack + 1):
            if weights_knapsack[i - 1] <= w:
                the_table[i][w] = max(values_knapsack[i - 1] + the_table[i - 1][w - weights_knapsack[i - 1]], the_table[i - 1][w])
            else:
                the_table[i][w] = the_table[i - 1][w]

    return the_table[n][capacity_knapsack]

weights_knapsack = [10, 20, 30, 40, 50]
values_knapsack = [40, 60, 80, 100, 120]
capacity_knapsack = 50
result_knapsack = knapsack_function(weights_knapsack, values_knapsack, capacity_knapsack)
print("0/1 Knapsack (DP):", result_knapsack)


# Longest Common Subsequence (LCS)
# Find the longest sequence in both given strings

def lcs_function(string_one, string_two):
    m, n = len(string_one), len(string_two)
    lcs_table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string_one[i - 1] == string_two[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])

    return lcs_table[m][n]

string_one = "AGGTAB"
string_two = "GXTXAYB"
lcs_results = lcs_function(string_one, string_two)
print("Longest Common Subsequence (DP):", lcs_results)


# Levenshtein Distance
# Find the min number of insertions, deletions or substitutions
# Then convert one string into another

def levenshtein_function(levstring_one, levstring_two):
    m, n = len(levstring_one), len(levstring_two)
    lev_table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                lev_table[i][j] = j
            elif j == 0:
                lev_table[i][j] = i
            elif levstring_one[i - 1] == levstring_two[j - 1]:
                lev_table[i][j] = lev_table[i - 1][j - 1]
            else:
                lev_table[i][j] = 1 + min(lev_table[i - 1][j],
                                          lev_table[i][j- 1],
                                          lev_table[i - 1][j - 1])
    return lev_table[m][n]

levstring_one = "kitchen"
levstring_two = "table"
levenshtein_result = levenshtein_function(levstring_one, levstring_two)
print("Edit Distance (DP):", levenshtein_result)