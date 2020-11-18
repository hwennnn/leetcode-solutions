class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort(key = lambda x: (x[0], x[1]))
        
        res = []
        res.append(intervals[0])
        curr = res[0]
        
        for x,y in intervals:
            if x <= curr[1]:
                curr[1] = max(curr[1], y)
            else:
                res.append([x,y])
                curr = res[-1]
        
        return res