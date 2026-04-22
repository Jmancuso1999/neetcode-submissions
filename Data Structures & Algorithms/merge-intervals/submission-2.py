class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        mergedIntervals = []
        prevInterval = intervals[0]
        for idx in range(1, len(intervals)):
            print(prevInterval)
            if intervals[idx][0] > prevInterval[1]:
                mergedIntervals.append(prevInterval)
                prevInterval = intervals[idx]
            else:
                prevInterval = [min(intervals[idx][0], prevInterval[0]), max(intervals[idx][1], prevInterval[1])]
        
        mergedIntervals.append(prevInterval)
        return mergedIntervals