class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split("/")
        stack = []
        
        for x in s:
            if x == "..":
                if stack:
                    stack.pop()
            elif x != "" and x != ".":
                stack.append(x)

        return "/" + "/".join(stack)