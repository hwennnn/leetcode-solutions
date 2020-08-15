class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        n = len(intervals)
        
        if n < 2: return 0
        
        intervals.sort(key = lambda x : x[0])
        
        last = intervals[0][1]
        count = 0
        
        for pairs in intervals[1:]:
            if pairs[0] < last:
                count += 1
                last = min(pairs[1], last)
                
            else:
                last = pairs[1]
            
            
        
        return count