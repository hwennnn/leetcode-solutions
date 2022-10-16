class Solution:
    def isValid(self, s: str) -> bool:
        mp = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        
        for x in s:
            if x in mp:
                if not stack or stack[-1] != mp[x]:
                    return False
                stack.pop()
            else:
                stack.append(x)
        
        return len(stack) == 0