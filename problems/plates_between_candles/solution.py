class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        A = [i for i, x in enumerate(s) if x == '|']
        res = []
        
        for start, end in queries:
            i = bisect.bisect_left(A, start)
            j = bisect.bisect(A, end) - 1
            res.append(A[j] - A[i] - (j - i) if i < j else 0)
        
        return res