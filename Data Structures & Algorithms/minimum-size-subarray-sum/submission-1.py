class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minCount = float('inf')
        left = 0
        currSum = 0

        for right in range(len(nums)):
            currSum += nums[right]
            while left <= right and currSum >= target:
                minCount = min(minCount, right - left + 1)
                currSum -= nums[left]
                left += 1

        if minCount == float('inf'):
            return 0
        
        return minCount
"""
[2,1,5,1,5,3]

- Dont think we can sort, sorting is out.

Brute Force:
1. Iterate every combination until target >= 10, see the total # 
   of values used.

Approach (sliding window) - O(n):
1. Move right pointer until sum >= target
2. When sum is >= target we move left pointer forward
"""