# Bottom Up - Time: O(n*t) where n is the length of the array and is t is the amount, space: O(t)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # DOESNT WORK --> Some conditional breaks this
        # for coin in coins:
        #     dp[coin] = 1
        
        # dp [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
        for amt in range(1, amount + 1): # No coin such as 1
            for coin in coins:
                if amt - coin >= 0: #EX: amt = 2, coin = 1
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin]) # need to check if a coin exists in that spot
        
        if dp[-1] == amount + 1:
            return -1
    
        return dp[-1]

"""
# Top Down - Time: O(n*t), Space: O(t) where is length of coins and t is the amount
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            elif amount < 0:
                return float('inf')
            if amount in memo:
                return memo[amount]

            minAmount = float('inf')
            for coin in coins:
                minAmount = min(minAmount, 1 + dfs(amount - coin))
                memo[amount] = minAmount 
        
            return minAmount

        minAmount = dfs(amount)

        if minAmount == float('inf'):
            return -1
        
        return minAmount


# Recursive - n^t - where n is length of coins and t is amount
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def dfs(amount):
            if amount == 0:
                return 0
            elif amount < 0:
                return float('inf')

            minAmount = float('inf')
            for coin in coins:
                minAmount = min(minAmount, 1 + dfs(amount - coin))
        
            return minAmount

        minAmount = dfs(amount)

        if minAmount == float('inf'):
            return -1
        
        return minAmount
"""