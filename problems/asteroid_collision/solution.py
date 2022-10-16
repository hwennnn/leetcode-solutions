class Solution:
    def asteroidCollision(self, A: List[int]) -> List[int]:
        n = len(A)
        stack = []
        
        for x in A:
            while stack and (x < 0 and stack[-1] > 0):
                if stack[-1] == -x:
                    stack.pop()
                    break
                    
                elif stack[-1] > -x:
                    break
                
                else:
                    stack.pop()
            
            else:
                stack.append(x)
        
        return stack
                