class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = float('-inf') 
        cnt = 0

        for interval in intervals:
            if interval[0] >= end:  
                end = interval[1]  
            else:
                cnt += 1
        return cnt