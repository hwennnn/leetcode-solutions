class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def convert(word):
            stack = []
            
            for w in word:
                if w == "#":
                    if len(stack) > 0:
                        stack.pop()
                
                else:
                    stack.append(w)
                    
            return "".join(stack)
        
        return convert(S) == convert(T)
            
                
            
        
        