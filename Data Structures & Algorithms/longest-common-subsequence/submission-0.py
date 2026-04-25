class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        currRow = [0] * len(text1)

        for pos1 in range(len(text1)):
            for pos2 in range(pos1, len(text2)):
                if text1[pos1] == text2[pos2]:
                    currRow[pos1] += 1
        
        return max(currRow)
"""
    c r a b t
  c 1 1 1 1 1
  a 1 1 2 2 2
  t 1 1 2 2 3

if text1[pos1] == text2[pos]:
    1 + max(dp[row - 1][col], dp[row][col - 1])

currRow = [0] * max(len(text1), len(text2))
after iterating each row, we set the new curr row to prev and build on top of that, then just return the 
last element of the row
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