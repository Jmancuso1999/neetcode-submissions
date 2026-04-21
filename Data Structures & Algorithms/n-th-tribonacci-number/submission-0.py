class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        dp = [n + 1] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for currNum in range(3, n + 1):
            dp[currNum] = dp[currNum - 1] + dp[currNum - 2] + dp[currNum - 3]
        
        return dp[-1]
"""
class Solution:
    def __init__(self):
        self.memoization = {}

    def tribonacci(self, n: int) -> int:
        return self.dfs(n)

    def dfs(self, n):
        if n <= 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        if n in self.memoization:
            return self.memoization[n]
        
        self.memoization[n] = self.dfs(n - 1) + self.dfs(n - 2) + self.dfs(n - 3)
        return self.memoization[n]
"""

