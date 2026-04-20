class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boatCount = 0

        while left <= right:
            sumTwoPeople = people[left] + people[right]

            if sumTwoPeople <= limit:
                boatCount += 1
                left += 1
                right -= 1
            else:
                boatCount += 1
                right -= 1

        return boatCount
"""
[5,1,4,2]
[5,4,2,1]
   ^ ^

[2,3,4,5]
^  ^ ^ ^

[1,2,2,3,3] limit = 3

if sumTwoPeople <= limit:
    boatCount += 1
    left += 1
    right -= 1
elif sumTwoPeople > limit:
    boatCount += 1
    right -= 1

"""