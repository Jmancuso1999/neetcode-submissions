class Solution:
    # Memoization (Top Down) - O(n^2)
    def __init__(self):
        self.memoization = {}

    def countSubstrings(self, s: str) -> int:
        totalPalidromes = 0

        for pos in range(len(s)):
            # Odd palidromes
            totalPalidromes += self.dfs(s, pos, pos)
            # Even palidromes
            totalPalidromes += self.dfs(s, pos, pos + 1)
        
        return totalPalidromes
        
    def dfs(self, word, left, right):
        if left < 0 or right >= len(word) or word[left] != word[right]:
            return 0
        if (left, right) in self.memoization:
            return self.memoization[(left, right)]

        res = 1 + self.dfs(word, left - 1, right + 1)
        self.memoization[(left, right)] = res
        return res

"""
# Recurive Approach O(2^n) where n is the length of S
class Solution:
    def countSubstrings(self, s: str) -> int:
        totalPalidromes = 0

        for pos in range(len(s)):
            # Odd palidromes
            totalPalidromes += self.dfs(s, pos, pos)
            # Even palidromes
            totalPalidromes += self.dfs(s, pos, pos + 1)
        
        return totalPalidromes
        
    def dfs(self, word, left, right):
        if left < 0 or right >= len(word) or word[left] != word[right]:
            return 0
        
        res = 1 + self.dfs(word, left - 1, right + 1)
        return res
"""