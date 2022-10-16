class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for x in num:
            while k > 0 and stack and stack[-1] > x:
                stack.pop()
                k -= 1
            
            stack.append(x)
            
        
        while stack and k > 0:
            stack.pop()
            k -= 1
        
        
        for i in range(len(stack)):
            if stack[i] == '0': continue
            
            return "".join(stack[i:])
        
        return "0"
            
            