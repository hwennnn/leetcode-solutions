class Solution:
    def __init__(self):
        self.dic = {0:0,1:1}
    def fib(self, N: int) -> int:
        
        if N in self.dic: return self.dic[N]
        
        val = self.fib(N-1) + self.fib(N-2)
        self.dic[N] = val
        
        return val