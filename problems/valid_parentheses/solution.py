class Solution:
    def isValid(self, S: str) -> bool:
        
        d = {")":"(", "}":"{", "]":"["}
        
        stack = []
        
        for s in S:
            
            if stack and s in d and stack[-1] == d[s]:
                stack.pop()
            else:
                stack.append(s)
        
        return len(stack) == 0
        