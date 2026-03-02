

def find_momentum_days(prices):
    momentum_days = []

    yesterday_change = prices[1] - prices[0]

    for i in range(2, len(prices)):
        current_change = prices[i] - prices[i - 1]

        if current_change > 0 and current_change > yesterday_change:
            momentum_days.append(i)

        yesterday_change = current_change

    return momentum_days
    pass


# Test
prices = [100, 102, 105, 107, 106, 108, 112, 114]
result = find_momentum_days(prices)
print(f"Momentum days: {result}")  # Expected: [2, 5, 6]
