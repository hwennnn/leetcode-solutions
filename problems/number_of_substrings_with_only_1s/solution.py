class Solution:
    def numSub(self, S: str) -> int:
        
        M = int(1e9+7)
        count = res = 0
        for s in S:
            count = count + 1 if s == "1" else 0
            res += count
        
        return res%M