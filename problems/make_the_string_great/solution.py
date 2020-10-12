class Solution:
    def makeGood(self, S: str) -> str:
        
        stack = []
        
        for s in S:
            
            if stack and (stack[-1] != s and stack[-1].lower() == s.lower()):
                stack.pop()
            else:
                stack.append(s)
        
        return "".join(stack)
                