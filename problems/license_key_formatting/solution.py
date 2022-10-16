class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.split('-')
        words = "".join(s)
        n = len(words)
        
        M = n % k
        start = M if M != 0 else k
        res = []
        res.append(words[:start].upper())

        for i in range(start, n, k):
            res.append(words[i : min(n, i + k)].upper())
        
        return "-".join(res)
        
        
                
            