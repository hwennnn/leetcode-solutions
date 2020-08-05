class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        stack = 0
        i = 0
        
        while n > stack:
            stack = stack + 1
            i += 1
            n -= stack
            
        return i
            
            
            

        
        