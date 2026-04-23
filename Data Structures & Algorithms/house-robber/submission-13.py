class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
            
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for idx in range(2, len(nums)):
            dp[idx] = max(dp[idx - 1], nums[idx] + dp[idx - 2])
        
        return dp[-1]
"""
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
"""
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.dfs(nums, 0)

    def dfs(self, nums, pos):
        if pos >= len(nums):
            return 0
        
        return max(self.dfs(nums, pos + 1), nums[pos] + self.dfs(nums, pos + 2))
"""