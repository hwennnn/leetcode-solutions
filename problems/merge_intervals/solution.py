class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals: return []
        
        intervals = sorted(intervals, key = lambda x : (x[0],x[1]))
        
        res = []
        curr = intervals[0]
        res.append(curr)
        
        for x in intervals[1:]:
            c1 = curr[0]
            c2 = curr[1]
            n1 = x[0]
            n2 = x[1]
            
            if c2 >= n1:
                curr[1] = max(c2,n2)
            
            else:
                curr = x
                res.append(curr)
        
        return res
        