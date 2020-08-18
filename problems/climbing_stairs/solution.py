class Solution:
    def __init__(self):
        self.mem = {0:0, 1:1, 2:2}
        
    def climbStairs(self, n: int) -> int:
        
        def climb(x):
            if x in self.mem: return self.mem[x]
            
            self.mem[x] = climb(x-1) + climb(x-2)
            
            return self.mem[x]
        
        return climb(n)
            