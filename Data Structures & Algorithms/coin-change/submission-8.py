class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memoization = {}

        def dfs(coins, amount):
            if amount == 0:
                return 0
            elif amount < 0:
                return float('inf')
            elif amount in memoization:
                return memoization[amount]

            res = float('inf')
            for coin in coins:
                res = min(res, 1 + dfs(coins, amount - coin))
                memoization[amount] = res
            
            return res
        
        minCount = dfs(coins, amount)

        if minCount == float('inf'):
            return -1
        
        return minCount