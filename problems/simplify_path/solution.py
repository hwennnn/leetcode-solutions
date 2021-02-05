class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split('/')
        
        ans = "/"
        stack = []
        for s in p:
            if s == "" or s == ".": continue
                
            if s == "..": 
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        
        return ans + "/".join(stack)