class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        numLength = len(nums)
        largestProduct = nums[0]
        prefix = 1
        suffix = 1

        for pos in range(numLength):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            
            prefix *= nums[pos] # Iterating from the front
            suffix *= nums[numLength - pos - 1] # Iterating from the back

            largestProduct = max(largestProduct, prefix, suffix)
        
        return largestProduct
"""
[1,2,-1,4,3,-6,2,-5] - suffix would give us 720

If we see a 0 like [1, 0,-1,4] - turn 0 to 1 using prefix/suffix method


"""

"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        totalMax = nums[0]

        for i in range(len(nums)):
            currMax = nums[i] 
            for j in range(i + 1, len(nums)):
                totalMax = max(totalMax, currMax)
                currMax *= nums[j]   

            totalMax = max(totalMax, currMax)
        
        return totalMax
"""