class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        n = len(s)
        
        for i in range(0, n, k):
            if i + k <= n:
                res.append(s[i:i + k])
            else:
                c = s[i : n]
                left = k - len(c)
                
                res.append(c + fill * left)
        
        
        return res