class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        res = []
        
        while k > 0 and n > 0:
            if (26 + n) <= k:
                res.append('z')
                k -= 26
                n -= 1
            else:
                if n == 1:
                    t = k % 27
                    res.append(chr(t+96))
                    k -= t
                    n -= 1
                else:
                    t = (k-n+1) % 27
                    res.append(chr(t+96))
                    k -= t
                    n -= 1
        
        res.sort()
        
        return "".join(res)