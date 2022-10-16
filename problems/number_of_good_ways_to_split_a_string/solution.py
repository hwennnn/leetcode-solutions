class Solution:
    def numSplits(self, S: str) -> int:
        n = len(S)
        prefix = [None] * n
        suffix = [None] * n
        mp = set()
        res = 0
        
        for i in range(n):
            mp.add(S[i])
            prefix[i] = len(mp)
            
        mp.clear()
        
        for i in reversed(range(n)):
            mp.add(S[i])
            suffix[i] = len(mp)
        

        for i in range(1,n):
            res += prefix[i-1] == suffix[i]
        
        return res