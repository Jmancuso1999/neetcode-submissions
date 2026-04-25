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