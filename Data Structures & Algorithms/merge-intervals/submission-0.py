class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort 
        intervals.sort(key = lambda x: x[0])
        res = []
        prevInterval = intervals[0]

        for pos in range(len(intervals)):
            currInterval = intervals[pos]
            if currInterval[0] <= prevInterval[1]:
                prevInterval = [min(prevInterval[0], currInterval[0]), max(prevInterval[1], currInterval[1])]
            else:
                res.append(prevInterval)
                prevInterval = currInterval
        
        res.append(prevInterval)
        return res

"""
[[1,3], [4,6], [5,8], [15,18]]

prevInterval = [1,3]
if currPos[0] <= prevInterval[1]:
    prevIntetval = [1, 6]
else:
    res.append(prevInterval)
    prevInterval = currPos

"""

