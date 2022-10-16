class Solution:
    def maxRepOpt1(self, text: str) -> int:
        A = [[c, len(list(x))] for c,x in itertools.groupby(text)]
        count = collections.Counter(text)
        
        res = max(min(count[c], x + 1) for c,x in A)
        
        for i in range(1, len(A) - 1):
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i - 1][0]]))
        
        return res