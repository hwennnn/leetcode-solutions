class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        stack = []
        res = [""] * n
        
        for i, x in enumerate(s):
            if x == "(":
                stack.append((x, i))
            elif x == ")":
                if stack and stack[-1][0] == "(":
                    ele, index = stack.pop()
                    res[index] = ele
                    res[i] = x
                else:
                    if stack:
                        stack.pop()
            else:
                res[i] = x
        
        return "".join(res)