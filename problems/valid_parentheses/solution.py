class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")":"(", "]":"[", "}":"{"}
        stack = []
        
        for e in s:
            if stack and (e in dic and stack[-1] == dic[e]):
                stack.pop()
            
            else:
                stack.append(e)
        
        return not stack
        