class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dp = [float('inf')] * (COLS + 1)
        dp[COLS - 1] = 0

        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                dp[col] = grid[row][col] + min(dp[col], dp[col + 1])

        return dp[0]
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dp = [[float('inf')] * (COLS + 1) for _ in range(ROWS + 1)]
        dp[ROWS - 1][COLS] = 0

        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                dp[row][col] = grid[row][col] + min(dp[row + 1][col], dp[row][col + 1])

        return dp[0][0]
"""
"""
Input: grid = [     Output: 8
    [1,2,0],
    [5,4,2],
    [1,1,3]
]

[
    [float('inf'), float('inf'), float('inf'), float('inf')],
    [float('inf'), float('inf'), float('inf'), float('inf')],
    [float('inf'), float('inf'), float('inf'), float('inf')],
    [float('inf'), float('inf'), float('inf'), float('inf')]
]
"""
"""
# Memoization (bottom up) - O(M * N)
class Solution:
    def __init__(self):
        self.memoization = {}

    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.dfs(grid, 0, 0)

    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return float('inf')
        elif row == len(grid) - 1 and col == len(grid[0]) - 1:
            return grid[row][col]
        elif (row, col) in self.memoization:
            return self.memoization[(row, col)]
        
        res = grid[row][col] + min(self.dfs(grid, row + 1, col), self.dfs(grid, row, col + 1))
        self.memoization[(row, col)] = res
        
        return res
"""
"""
# Recursive DFS - O(2^(m+n))
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.dfs(grid, 0, 0)

    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return float('inf')
        elif row == len(grid) - 1 and col == len(grid[0]) - 1:
            return grid[row][col]
        
        res = grid[row][col] + min(self.dfs(grid, row + 1, col), self.dfs(grid, row, col + 1))
        
        return res
"""