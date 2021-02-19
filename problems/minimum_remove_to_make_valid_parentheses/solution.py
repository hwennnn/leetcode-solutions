class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ""
        stack = []
        mp = {}
        
        for i,c in enumerate(s):
            if c == ")" and stack and stack[-1][1] == "(":
                x, p = stack.pop()
                mp[x] = p
                mp[i] = c
                
            elif c == "(":
                stack.append((i,c))
        
        
        for i,c in enumerate(s):
            if c == "(" or c == ")":
                if i in mp:
                    res += mp[i]
            else:
                res += c
        
        return res
