class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        last = []
        
        while k >= 26 + n:
            last.append("z")
            n -= 1
            k -= 26
            
        first = []
        for i in range(n):
            if i == n - 1:
                first.append(chr(ord("a") + k - 1))
            else:
                first.append("a")
                k -= 1
        
        return "".join(first + last)