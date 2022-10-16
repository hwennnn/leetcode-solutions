class Solution:
    def findMaxAverage(self, A: List[int], K: int) -> float:
        
        s = 0
        m = float('-inf')
        
        for i,x in enumerate(A):
            s += x
            
            if i >= K:
                s -= A[i-K]
            
            if i >= K-1:
                m = max(m, s)
        
        return m / K 