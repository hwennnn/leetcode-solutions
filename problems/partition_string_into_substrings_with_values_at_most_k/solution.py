class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        N = len(s)
        curr = 0
        res = 0
        
        for x in s:
            x = int(x)
            
            curr = curr * 10 + x
            
            if curr > k:
                res += 1
                curr = x
            
            if curr > k: return -1

        return res + 1
            
            