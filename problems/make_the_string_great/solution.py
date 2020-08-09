class Solution:
    def makeGood(self, s: str) -> str:
        
        n = len(s)
        
        stack = []
        
        for i in range(n):
            
            if stack and abs(ord(stack[-1])-ord(s[i])) == 32:
                stack.pop()
            
            else:
                stack.append(s[i])
        

        return "".join(stack)
                
                