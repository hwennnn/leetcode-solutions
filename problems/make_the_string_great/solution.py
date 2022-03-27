class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for x in s:
            stack.append(x)
            while len(stack) >= 2 and stack[-1] != stack[-2] and stack[-1].upper() == stack[-2].upper():
                stack.pop()
                stack.pop()
        
        return "".join(stack)
            