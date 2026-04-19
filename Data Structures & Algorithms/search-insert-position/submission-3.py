class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[len(nums) - 1]:
            return len(nums)
        if target < nums[0]:
            return 0

        left = 0
        right = len(nums) - 1
        res = len(nums)
        
        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        
        return res

"""
Brute Force:
1. Iterate through until we find a value >= target

Optimal: 
1. target > all elements in nums - append at len(nums)
2. target < all elements in nums - append at 0
3. Otherwise iterate through and find the pos

left = 3
right = 5
mid = 4
target < nums[mid]:
    right = mid - 1


left =3
right = 4


"""