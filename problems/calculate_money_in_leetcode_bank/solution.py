class Solution:
    def totalMoney(self, n: int) -> int:
        res = times = 0
        c = 1
        
        for _ in range(n):
            if c == 8: 
                c = 1
                times += 1
            
            res += c + times
            c += 1
            
        return res