class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        k = 1
        for interval in intervals[1:]:
            if interval[0] >= end:
                k+=1
                end = interval[1]
            
        return n - k
        