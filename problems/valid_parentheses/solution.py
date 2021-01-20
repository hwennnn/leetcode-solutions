class Solution:
    def isValid(self, s: str) -> bool:
        mp = {")":"(", "}":"{", "]":"["}
        stack = []
        
        for c in s:
            if c in mp:
                if stack and stack[-1] == mp[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0