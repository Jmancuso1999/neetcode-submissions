class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0

        for num in nums:
            currSum += num

            maxSum = max(maxSum, currSum)
            if currSum < 0:
                currSum = 0
        
        return maxSum

"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        for left in range(len(nums)):
            currSum = 0
            for right in range(left, len(nums)):
                currSum += nums[right]
                maxSum = max(maxSum, currSum)

                if currSum < 0:
                    break

        return maxSum
"""
