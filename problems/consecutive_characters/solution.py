class Solution:
    def maxPower(self, S: str) -> int:
        if not S: return 0
        res = c = 1
        
        for i in range(1,len(S)):
            if S[i] == S[i-1]:
                c += 1
                res = max(res, c)
            else:
                c = 1
            
        return res
            