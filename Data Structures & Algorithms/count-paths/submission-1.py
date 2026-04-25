# Bottom Up O(m*n) time and O(n) space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for r in range(m - 1):
            currRow = [1] * n
            for c in range(n - 2, -1, -1): # We dont need the last col since its always 1
                currRow[c] = currRow[c + 1] + row[c] # row[col] = row + 1, col (below currNow)

            row = currRow

        return row[0]
"""
m = 3, n = 6
21  15  10  6   3   1   # Second iteratiobn of the for j in range....
6   5    4  3   2   1   # First iteration of the for j in range....
1   1    1  1   1   1 

# Top Down and far right column will always be 1
"""
"""
Bottom Up - O(m * n) time and space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)] # Space: O(m * n)

        # Time: O(m * n)
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    continue
                else:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[-1][-1]
"""
"""
Brute Force: O(2^(m + n))
        return self.dfs(m,n, 0, 0)
    
    def dfs(self, m, n, currM, currN):
        if currM == m - 1 and currN == n - 1:
            return 1
        elif m < 0 or n < 0 or currM >= m or currN >= n:
            return 0
        
        res = self.dfs(m, n, currM + 1, currN) + self.dfs(m, n, currM, currN + 1)

        return res
"""