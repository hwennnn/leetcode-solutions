class Solution:
    def replaceDigits(self, s: str) -> str:
        res = []
        
        for i, c in enumerate(s):
            if c.isnumeric():
                res.append(chr(ord(s[i-1]) + int(c)))
            else:
                res.append(c)
        
        return "".join(res)