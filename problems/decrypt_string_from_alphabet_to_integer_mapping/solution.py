class Solution:
    def freqAlphabets(self, s: str) -> str:
        n = len(s)
        i = 0
        res = []
        
        while i < n:
            if i + 2 < n and s[i + 2] == "#":
                c = int(s[i : i + 2]) - 1
                res.append(chr(ord('a') + c))
                i += 3
            else:
                c = int(s[i]) - 1
                res.append(chr(ord('a') + c))
                i += 1
        
        return "".join(res)