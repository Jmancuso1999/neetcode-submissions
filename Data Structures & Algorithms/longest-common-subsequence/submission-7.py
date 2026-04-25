
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        prevRow = [0] * (len(text2) + 1)
        currRow = [0] * (len(text2) + 1)

        for pos1 in range(len(text1) -1 , -1, -1):
            for pos2 in range(len(text2) - 1, -1, -1):
                if text1[pos1] == text2[pos2]:
                    currRow[pos2] = 1 + prevRow[pos2 + 1]
                else:
                    currRow[pos2] = max(prevRow[pos2], currRow[pos2 + 1])
                
                # update the prev row with the curr once
            prevRow, currRow = currRow, prevRow
            
        return prevRow[0]
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