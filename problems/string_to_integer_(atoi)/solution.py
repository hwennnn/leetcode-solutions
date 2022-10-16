class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1
        
        n = len(s)
        res = i = 0
        
        while i < n and s[i] == " ":
            i += 1
        
        if i == n: return 0
        
        is_negative = False
        if s[i] == "-":
            is_negative = True
        
        if s[i] in '+-':
            i += 1
        
        while i < n and s[i].isdecimal():
            res = res * 10 + int(s[i])
            i += 1
        
        if is_negative:
            res *= -1
        
        return max(INT_MIN, min(res, INT_MAX))