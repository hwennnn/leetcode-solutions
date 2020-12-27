class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        n = len(s)
        i = 0
        
        while i < n:
            
            if i + 2 < n and s[i+2] == "#" and 10 <= int(s[i:i+2]) <= 26:
                res.append(chr(ord('a') + int(s[i:i+2]) - 1))
                i += 3
            
            else:
                res.append(chr(ord('a') + int(s[i]) - 1))
                i += 1
        
        return "".join(res)