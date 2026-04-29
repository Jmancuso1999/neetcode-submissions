class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arrayTotal = sum(nums) 
        if arrayTotal % 2 == 1:
            return False

        # TRACE PROBLEM TO SEE 0/1 KNAPSACK
        

        target = arrayTotal // 2
        # O/1 Knapsack problem
        dp = [[-1] * (target + 1) for _ in range(len(nums) + 1)] 
        # Doing -1 since True / False evaluates to 0 or 1
    
        def dfs(nums, pos, target):
            if target == 0:
                return True
            elif pos >= len(nums) or target < 0:
                return False
            if dp[pos][target] != -1:
                return dp[pos][target]

            dp[pos][target] = (dfs(nums, pos + 1, target - nums[pos]) or dfs(nums, pos + 1, target))

            # Should return bottom right of 2-d array since this is 0/1 knapsack problem
            return dp[pos][target]

        return dfs(nums, 0, target)
"""
class Solution:
    # O(2^N)
    def canPartition(self, nums: List[int]) -> bool:
        arrayTotal = sum(nums) 
        if arrayTotal % 2 == 1:
            return False

        return self.dfs(nums, 0, arrayTotal // 2)
    
    def dfs(self, nums, pos, target):
        if pos >= len(nums):
            return target == 0
        elif target < 0:
            return False
        
        subtractVal = self.dfs(nums, pos + 1, target - nums[pos]) 
        ignoreVal = self.dfs(nums, pos + 1, target)
"""
"""
If the total amount of values in the array add up to 10, we just need to check if the total of 
ONE subarray adds up to 5.

This is a 0/1 Knapsack problem
"""