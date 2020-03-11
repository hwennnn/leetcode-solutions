class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) < 2: return 0
        
        intervals.sort(key = lambda x: x[0])
        
        curr_end, count = intervals[0][1], 0
        
        for i in intervals[1:]:
            if i[0] < curr_end:
                count += 1
                curr_end = min(i[1], curr_end)
                
            else:
                curr_end = i[1]
                
        return count