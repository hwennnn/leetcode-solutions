class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ''
        
        for c in s:
            if ord('A') <= ord(c) <= ord('Z'):
                v = (ord(c) - ord('A'))
                res += chr(ord('a') + v)
            else:
                res += c

        
        return res