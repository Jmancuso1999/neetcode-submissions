class Solution:
    def __init__(self):
        self.memoization = {}

    def rob(self, nums: List[int]) -> int:
        return self.dfs(nums, 0)

    def dfs(self, nums, pos):
        if pos >= len(nums):
            return 0
        if pos in self.memoization:
            return self.memoization[pos]
        
        res = max(self.dfs(nums, pos + 1), nums[pos] + self.dfs(nums, pos + 2))
        self.memoization[pos] = res

        return res