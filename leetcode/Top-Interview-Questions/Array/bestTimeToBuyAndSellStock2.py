
def maxProfit(prices):
    profit = 0
    for i in range(0, len(prices)-1):
        if prices[i] < prices[i+1]:
            profit += prices[i+1]-prices[i]
    
    return profit
    



prices = [7,6,4,3,4]

print(maxProfit(prices))