class Solution:
    # Bottom Up - Gives us the same time and space as Top Down
    # Time: O(n*t) where n is the # of coins and t is the total amount 
    # Space: O(t) where t is the amount
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for currAmt in range(1, amount + 1):
            for coin in coins:
                if currAmt - coin >= 0:
                    dp[currAmt] = min(1 + dp[currAmt - coin], dp[currAmt])

        if dp[-1] == float('inf'):
            return -1
        
        return dp[-1]
    
"""
class Solution:
    # Top Down Approach
    # Time: O(n*t) where n is the # of coins and t is the total amount 
    # Space: O(t) where t is the amount
    def __init__(self):
        self.memoization = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
        minAmount =  self.dfs(coins, amount)

        if minAmount == float('inf'):
            return -1
        
        return minAmount
    
    def dfs(self, coins, amount):
        if amount == 0:
            return 0
        elif amount < 0:
            return float('inf')
        
        if amount in self.memoization:
            return self.memoization[amount]

        res = float('inf')
        for coin in coins:
            res = min(res, 1 + self.dfs(coins, amount - coin))
            self.memoization[amount] = res
        
        return res
"""
"""
class Solution:
    # Recursive Solution - O(n^t) - n == # of coins and t == amount
    def coinChange(self, coins: List[int], amount: int) -> int:
        minAmount =  self.dfs(coins, amount)

        if minAmount == float('inf'):
            return -1
        
        return minAmount
    
    def dfs(self, coins, amount):
        if amount == 0:
            return 0
        elif amount < 0:
            return float('inf')
        
        res = float('inf')
        for coin in coins:
            res = min(res, 1 + self.dfs(coins, amount - coin))
        
        return res
"""
"""
            12
    2                   7
-8 -3   1         -3    2   6  
    -11 -4 0            

"""