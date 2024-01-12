# Time O(n) | Space O(1)
def buy_and_sell_stock_once(prices: list[float]) -> float:
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


prices = [310, 315, 260, 270, 290, 230, 255, 250]
print(buy_and_sell_stock_once(prices))