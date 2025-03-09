# Greedy Algorithms
# Chooses which looks best at that exact moment
# Tries to achieve a global optimum
import heapq

# Coin Change Problem
# Use the fewest amount of coins possible to get the target amount

def coin_change_greedy(coins, amount_coin_change):
    coins.sort(reverse=True)
    count = 0
    result = []

    for coin in coins:
        while amount_coin_change >= coin:
            amount_coin_change -= coin
            result.append(coin)
            count += 1

    if amount_coin_change == 0:
        return result, count
    else:
        return "Change not possible with given denominations"

coins = [25, 10, 5, 1]
amount_coin_change = 63
result_coin_change = coin_change_greedy(coins, amount_coin_change)
print("Coin Change (Greedy):", result_coin_change)


# Activity Problem Algorithm
# Find the maximum number of non-overlapping activities

def activity_selection_greedy(start_times, end_times):
    activities = sorted(zip(start_times, end_times), key=lambda x: x[1])
    selected_activities = [activities[0]]

    for i in range(1, len(activities)):
        if activities[i][0] >= selected_activities[-1][1]:
            selected_activities.append(activities[i])

    return selected_activities

start_times = [1, 3, 0, 5, 8, 5]
end_times = [2, 4, 6, 7, 9, 9]
result_activity = activity_selection_greedy(start_times, end_times)
print("Activity Selection (Greedy):", result_activity)


# Fractional Knapsack Problem
# Maximize the value by taking full or partial items
# Resource allocation

def fractional_knapsack(weights_knapsack, values_knapsack, capacity_knapsack):
    items = sorted(zip(weights_knapsack, values_knapsack), key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    selected_items = []

    for weight, value in items:
        if capacity_knapsack >= weight:
            capacity_knapsack -= weight
            total_value += value
            # 1 means full-item taken
            selected_items.append((weight, value, 1))
        else:
            fraction = capacity_knapsack / weight
            total_value += value * fraction
            selected_items.append((weight, value, fraction))
            break

        return selected_items, total_value
    
weights_knapsack = [10, 20, 30, 40, 50]
values_knapsack = [50, 70, 90, 110, 125]
capacity_knapsack = 100
result_knapsack = fractional_knapsack(weights_knapsack, values_knapsack, capacity_knapsack)
print("Fractional Knapsack (Greedy):", result_knapsack)



# Huffman Coding (File Compression)
# Variable length codes based on frequency of characters

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
    
def huffman_coding_function(frequencies_huffman):
    heap = [HuffmanNode(char, freq) for char, freq in frequencies_huffman.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        new_node = HuffmanNode(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        heapq.heappush(heap, new_node)

    def build_codes(node, code="", mapping={}):
        if node:
            if node.char is not None:
                mapping[node.char] = code
            build_codes(node.left, code + "0", mapping)
            build_codes(node.right, code + "1", mapping)
        return mapping

frequencies_huffman = {"a": 5, "b": 9, "c": 12, "d": 13, "e": 16, "f": 45}
result_huffman = huffman_coding_function(frequencies_huffman)
print("Huffman Coding (Greedy):", result_huffman)