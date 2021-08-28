class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : (x[0], -x[1]))
        res = []
        s, e = intervals[0]

        for start, end in intervals[1:]:
            if e >= start:
                e = max(e, end)
            else:
                res.append([s, e])
                s, e = start, end
                
        res.append([s, e])
        return res