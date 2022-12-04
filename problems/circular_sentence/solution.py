class Solution:
    def isCircularSentence(self, s: str) -> bool:
        s = s.split(" ")
        N = len(s)
        prev = s[0][-1]
        
        for i in range(1, N):
            start = s[i][0]
            
            if start != prev: return False
            
            prev = s[i][-1]
        
        if s[0][0] != prev: return False
        
        return True