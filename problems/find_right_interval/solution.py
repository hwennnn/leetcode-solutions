class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        A = sorted([(x, i) for i, (x, _) in enumerate(intervals)])

        res = []

        for start, end in intervals:
            index = bisect.bisect_left(A, (end, ))
            
            if index < n:
                res.append(A[index][1])
            else:
                res.append(-1)
        
        return res
        