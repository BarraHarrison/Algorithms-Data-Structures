# Greedy Algorithms
# Chooses which looks best at that exact moment
# Tries to achieve a global optimum

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