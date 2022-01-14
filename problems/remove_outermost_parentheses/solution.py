class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened = 0
        res = []
        
        for x in s:
            if opened > 0:
                res.append(x)
                
            if x == "(":
                opened += 1
            else:
                opened -= 1
                if opened == 0:
                    res.pop()
        
        return "".join(res)