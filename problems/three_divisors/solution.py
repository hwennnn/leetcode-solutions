class Solution:
    def isThree(self, n: int) -> bool:
        res = 0
        
        for k in range(1, n + 1):
            if n % k == 0: res += 1
            
            if res > 3: return False
        
        return res == 3