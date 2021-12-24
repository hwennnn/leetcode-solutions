class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start, end = intervals[0]
        res = []
        
        for s, e in intervals[1:]:
            if s <= end:
                end = max(end, e)
            else:
                res.append([start, end])
                start, end = s, e
                
        res.append([start, end])
        return res