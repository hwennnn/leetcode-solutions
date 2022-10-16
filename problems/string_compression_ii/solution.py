class Solution:
    def getLengthOfOptimalCompression(self, s: str, K: int) -> int:
        N = len(s)
        
        def countLength(x):
            if x == 0: return 0
            
            if x == 1: return 1
            
            return len(str(x)) + 1
        
        @cache
        def go(index, prev, prevCount, k):
            if k < 0: return inf
            
            if index == N: return countLength(prevCount)
            
            if s[index] != prev:
                return min(countLength(prevCount) + go(index + 1, s[index], 1, k), go(index + 1, prev, prevCount, k - 1))
            
            return min(go(index + 1, prev, prevCount + 1, k), go(index + 1, prev, prevCount, k - 1))
        
        return go(0, "", 0, K)