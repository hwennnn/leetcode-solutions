class Solution:
    def numEquivDominoPairs(self, A: List[List[int]]) -> int:
        n = len(A)
        mp = collections.defaultdict(int)
        
        def make(A):
            return (min(A), max(A))
        
        res = 0
        for i in range(n):
            m = make(A[i])
            res += mp[m]
            
            mp[m] += 1
        
        return res