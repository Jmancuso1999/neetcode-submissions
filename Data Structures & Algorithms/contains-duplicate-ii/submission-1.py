class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left  = 0

        for right in range(len(nums)):
            if right - left > k:
                window.remove(nums[left])
                left += 1
            
            # Since we are keeping track of the window we only need to look
            # for the duplicate
            if nums[right] in window:
                return True
            
            window.add(nums[right])

        return False
        
"""
Brute Force:
1. Nested for loop where we iterate over every combination and 
   validating if both conditionals if they are, return true.

Optional Approach:
(ORGINALLY I HAD THE WRONG OPTINAL APPROACH)

[1,2,3,6,5,7,8]
1,2,3,6 - checking k range first

2,3,6,5 - then update left + 1

First iterate left = 0
Looks like we can iterate like this:
1. for loop (right) in range of left + 1 to len(nums)
    if abs(left - right) > k:
        remove nums[left]
        left += 1
    
    if nums[left] == nums[right]: return True

"""