class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        sell = prices[n-1]
        profit=0
        for i in range(n-1):
            profit = max(profit, sell - prices[n-2-i])
            if sell < prices[n-2-i]:
                sell = prices[n-2-i]
        return profit
