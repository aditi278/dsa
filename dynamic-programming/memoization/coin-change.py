class Solution:
    def coinChange(self, coins: List[int], amount: int, memo=None) -> int:
        if memo is None:
            if amount == 0:
                return 0
            memo = {}
        if amount in memo:
            return memo[amount]
        count = sys.maxsize
        for i in range(len(coins)):
            diff = amount - coins[i]
            if diff > 0:
                last_count = self.coinChange(coins, diff, memo)
                if last_count != -1:
                    count = min(count, last_count+1)
            if diff == 0:
                return 1
        if count != sys.maxsize:
            memo[amount] = count
        else:
            memo[amount] = -1
        return memo[amount]