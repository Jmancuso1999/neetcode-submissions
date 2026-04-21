"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True

        intervals.sort(key = lambda time: time.start)
        prevInterval = intervals[0]

        for index in range(1, len(intervals)):
            if intervals[index].start < prevInterval.end:
                return False
            
            prevInterval = intervals[index]
        
        return True