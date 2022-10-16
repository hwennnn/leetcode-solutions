class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        n = len(s)
        
        res = 0
        
        for i in range(n - k + 1):
            x = s[i : i + k]
            
            if int(x) != 0 and num % int(x) == 0:
                res += 1
        
        return res