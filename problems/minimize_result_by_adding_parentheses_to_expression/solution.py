class Solution:
    def minimizeResult(self, expression: str) -> str:
        res = (float('inf'), None)
        s = list(expression)
        n = len(s)
        index = s.index("+")
        
        @cache
        def go(left, right):
            nonlocal res
            
            if left >= 0 and right <= n and left <= index and right >= index:
                t = s[:]
                t.insert(left, "(")
                t.insert(right + 2, ")")
            
                t = "".join(t)
                x = t[:]
                
                if left != 0:
                    x = t[:left] + "*" + t[left:]
                
                currN = len(x)
                rIndex = x.index(")")
                
                if rIndex + 1 < currN:
                    x = x[:rIndex + 1] + "*" + x[rIndex + 1:]
                try:
                    val = eval(x)
                    # print(x, val)
                    if val < res[0]:
                        res = (val, t)
                except:
                    pass
            else:
                return
            
            go(left - 1, right)
            go(left, right + 1)
            go(left - 1, right - 1)
        
        go(index - 1, index + 1)
        
        return res[1]