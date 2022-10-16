class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        res = s.count("0")
        val = 0
        base = 1
        
        for x in s[::-1]:
            if val + base > k: break
                
            if x == "1":
                res += 1
                val += base
        
            base *= 2
        
        return res
        