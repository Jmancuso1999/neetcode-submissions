class Solution:
    def __init__(self):
        self.memoization = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
        totalCoins = self.dfs(coins, amount)
        if totalCoins == float('inf'):
            return -1
        
        return totalCoins

    def dfs(self, coins, amt):
        if amt == 0:
            return 0
        elif amt < 0:
            return float('inf')

        if amt in self.memoization:
            return self.memoization[amt]

        res = float('inf')
        for coin in coins:
            res = min(res, 1 + self.dfs(coins, amt - coin))
            self.memoization[amt] = res
        
        return res