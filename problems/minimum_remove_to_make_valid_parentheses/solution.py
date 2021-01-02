class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        
        for i,c in enumerate(s):
            if c == ")":
                if stack: 
                    stack.pop()
                else:
                    s[i] = ""

            elif c == "(":
                stack.append(i)
            

        while stack:
            s[stack.pop()] = ""

        return "".join(s)