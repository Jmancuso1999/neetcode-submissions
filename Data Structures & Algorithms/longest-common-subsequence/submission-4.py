class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Bottom-Up - O(m * n) time and space
        # Need to do + 1 for both for the dp 2-d array when we check prevRow / prevCol
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for pos1 in range(len(text1) -1 , -1, -1):
            for pos2 in range(len(text2) - 1, -1, -1):
                if text1[pos1] == text2[pos2]:
                    dp[pos1][pos2] = 1 + dp[pos1 + 1][pos2 + 1]
                else:
                    dp[pos1][pos2] = max(dp[pos1 + 1][pos2], dp[pos1][pos2 + 1])

        return dp[0][0]

"""
# Top Down - O(m * n) time and Space
class Solution:
    def __init__(self):
        self.memoization = {}

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.dfs(text1, text2, 0, 0)
    
    def dfs(self, text1, text2, pos1, pos2):
        if pos1 >= len(text1) or pos2 >= len(text2):
            return 0
        if (pos1, pos2) in self.memoization:
            return self.memoization[(pos1, pos2)]

        if text1[pos1] == text2[pos2]:
            res = 1 + self.dfs(text1, text2, pos1 + 1, pos2 + 1)
            self.memoization[(pos1, pos2)] = res
            return res
        
        res = max(self.dfs(text1, text2, pos1 + 1, pos2), self.dfs(text1, text2, pos1, pos2 + 1))
        self.memoization[(pos1, pos2)] = res
        return res
"""
"""
# Reucursive approach - O(2^(m+n))
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.dfs(text1, text2, 0, 0)
    
    def dfs(self, text1, text2, pos1, pos2):
        if pos1 >= len(text1) or pos2 >= len(text2):
            return 0

        if text1[pos1] == text2[pos2]:
            return 1 + self.dfs(text1, text2, pos1 + 1, pos2 + 1)
        
        return max(self.dfs(text1, text2, pos1 + 1, pos2), self.dfs(text1, text2, pos1, pos2 + 1))
"""