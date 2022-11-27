class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        N, M = len(s), len(t)
        j = 0
        curr = 0
        
        for i, x in enumerate(s):
            if j == M: break
                
            if x == t[j]:
                curr += 1
                j += 1
        
        return M - curr
                