class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        
        while len(s) > 0:
            count = 0
            stack = []
            
            for x in s:
                if x == "a":
                    count = 1
                elif x == "b" and count == 1:
                    count = 2
                elif x == "c" and count == 2:
                    count = 3
                else:
                    count = 0
                    
                stack.append(x)
                
                if count == 3:
                    for _ in range(3):
                        stack.pop()
                    count = 0
            
            if len(s) == len(stack): return False
            s = stack
                
                
        return len(s) == 0