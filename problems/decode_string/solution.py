class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        stack = []
        
        for c in s:
            if c == "]":
                t = ""
                while stack[-1] != "[":
                    t = stack.pop() + t
                
                stack.pop()
                
                times = ""
                while stack and stack[-1].isnumeric():
                    times = stack.pop() + times
                
                stack.append(int(times)*t)
            
            else:
                stack.append(c)
        
        return "".join(stack)