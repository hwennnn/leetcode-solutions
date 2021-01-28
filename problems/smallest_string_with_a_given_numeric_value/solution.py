class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ["a" for _ in range(n)]
        k -= n
        
        for i in range(n-1, -1, -1):
            x = min(k, 25)
            k -= x
            res[i] = chr(ord('a') + x)
        
        return "".join(res)