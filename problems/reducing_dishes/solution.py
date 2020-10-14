class Solution:
    def maxSatisfaction(self, S: List[int]) -> int:
        S.sort()
        
        res = c = m = 0
        for i in reversed(range(len(S))):
            m += c + S[i]
            c += S[i]
            res = max(res, m)
            
        return res
        
        