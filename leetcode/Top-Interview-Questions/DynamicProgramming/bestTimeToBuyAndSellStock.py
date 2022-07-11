def maxProfit(prices):
  buy = 0
  sell = 1
  max_profit = 0
  while sell < len(prices):
    profit = prices[sell] - prices[buy]
    if prices[buy] < prices[sell]:
      max_profit = max(profit, max_profit)
    else:
      buy = sell
    sell += 1
  return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
