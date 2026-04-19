class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numCount = Counter(nums)

        for num, count in numCount.items():
            if count > len(nums) / 2:
                return num

"""
Are we guranteed 1 answer or multiple? Yes since we are doing MORE than
    n/2 it is guranteed 1 answer.

Brute Force:
1. Counter of all elements
2. Iterate the counter until we find an element > n/2 and return that element

Space Optimized: 
1. Sort it and count the current element and check if start - end + 1 > n/2
    - Time: O(n log n) with O(1) space

Space and Time Optimized:
BIT MANIPULATION (NO CLUE HOW TO DO)

"""