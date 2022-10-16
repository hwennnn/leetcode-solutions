class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = ""
        
        
        while a > 0 and b > 0:
            if a > b:
                res += "a" * min(a, 2)
                res += "b"
                a -= min(a, 2)
                b -= 1
            elif a == b:
                if not res or res[-1] == "a":
                    res += "b"
                    b -= 1
                else:
                    res += "a"
                    a -= 1
            else:
                res += "b" * min(b, 2)
                res += "a"
                b -= min(b, 2)
                a -= 1
        
        if a > 0:
            res += "a" * a
        
        if b > 0:
            res += "b" * b
        
        return res