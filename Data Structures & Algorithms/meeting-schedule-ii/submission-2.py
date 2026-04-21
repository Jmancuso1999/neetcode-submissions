"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)

        intervals.sort(key=lambda time: time.start)
        minHeap = []

        for index in range(len(intervals)):
            if minHeap and minHeap[0] <= intervals[index].start:
                heapq.heappop(minHeap)
            
            heapq.heappush(minHeap, intervals[index].end)
        
        return len(minHeap)

"""
[(1,5),(2,6),(3,7),(4,8),(5,9)]

minHeap = [5,6,7,8]
        = [6,7,8,9] - (5,9) position compares to minHeap[0] which is 5, so it pops 5

Time: O(n log n)
SpacE: O(n)
"""