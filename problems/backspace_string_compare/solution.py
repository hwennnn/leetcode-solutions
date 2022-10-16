class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def check(A):
            stack = []
            
            for x in A:
                if x == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(x)
            
            return stack
        
        return check(s) == check(t)