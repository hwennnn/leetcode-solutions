class Solution:
    def maxScore(self, S: str) -> int:
        res = 0
        for i in range(len(S)-1):
            a = S[:i+1].count("0")
            b = S[i+1:].count("1")
            res = max(res, a+b)
        
        return res