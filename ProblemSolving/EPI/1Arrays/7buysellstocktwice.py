# Now this is interesting! I couldn't figure this out by myself. Had to swallow the ego and had a look at the
# solution. This can be solved by having two passes; 1st: Like previous problem, find the max profit for one sale (
# for each day) 2nd: Go in reverse, i.e, for day x, find out what profit can be made for the remaining days from x
# till last day by one sale.
# Finally, combine both the profits by simply adding.
def buy_and_sell_stock_twice(prices: list[float]) -> float:
    # First pass, going forward:
    forward_profit = []
    min_price, max_profit = float('inf'), 0
    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
        forward_profit.append(max_profit)

    # Second Pass, going backward:
    backward_profit = []
    max_price = 0
    max_profit = 0
    for price in reversed(prices):
        max_profit = max(max_profit, max_price - price)
        max_price = max(max_price, price)
        backward_profit.append(max_profit)
    one_pass_max_profit = max_profit

    backward_profit = backward_profit[::-1]
    # print(forward_profit, '\n', backward_profit)
    max_profit = 0
    for i in range(len(forward_profit)):
        max_profit = max(max_profit, forward_profit[i] + backward_profit[i])

    # print(forward_profit)
    # print(backward_profit)
    return max_profit


# prices = [310, 315, 260, 270, 290, 230, 255, 250]
# prices = [12, 11, 13, 9, 12, 8, 14, 13, 15]
prices = [0.3, 0.1, 0.4, 0.1]
print(buy_and_sell_stock_twice(prices))
