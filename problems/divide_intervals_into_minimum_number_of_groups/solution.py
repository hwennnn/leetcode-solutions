class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        A = []
        
        for s, e in intervals:
            A.append((s, 1))
            A.append((e + 1, -1))
        
        A.sort()
        res = curr = 0
        
        for x, d in A:
            curr += d
            res = max(res, curr)
        
        return res