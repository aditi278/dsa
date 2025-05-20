class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        if n < 2:
            return 0
        for i in range(1, n):
            profit+=max(0, prices[i]-prices[i-1])
        return profit