class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        c = 0
        
        for i,x in enumerate(str(n)):
            p *= int(x)
            c += int(x)
        
        return p - c