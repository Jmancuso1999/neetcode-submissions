class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arrayTotal = sum(nums) 
        if arrayTotal % 2 == 1:
            return False

        target = arrayTotal // 2
        # O/1 Knapsack problem
        dp = [[-1] * (target + 1) for _ in range(len(nums) + 1)] 
        # Doing -1 since True / False evaluates to 0 or 1
    
        def dfs(pos, target):
            if target == 0:
                return True
            elif pos >= len(nums) or target < 0:
                return False
            elif dp[pos][target] != -1: # Means visited already
                return dp[pos][target]
            
            # We have 2 options for 0/1 Knapsack
            # 1. Take the value (1 - in this case subtract from total and increase pos)
            # 2. Leave the value (0 - in this case dont do anything just increase pos)
            dp[pos][target] = (dfs(pos + 1, target - nums[pos]) or dfs(pos + 1, target))

            # After the recursion we get back to this position that we started at
            return dp[pos][target]

        return dfs(0, target)
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
        
        takeVal = self.dfs(nums, pos + 1, target - nums[pos]) 
        leaveVal = self.dfs(nums, pos + 1, target)

        return takeVal or leaveVal
"""
"""
If the total amount of values in the array add up to 10, we just need to check if the total of 
ONE subarray adds up to 5.

This is a 0/1 Knapsack problem
"""