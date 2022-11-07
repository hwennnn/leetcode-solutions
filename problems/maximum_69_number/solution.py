class Solution:
    def maximum69Number (self, num: int) -> int:
        k = -1
        p = 0
        curr = num
        
        while curr > 0:
            d = curr % 10
            if d == 6:
                k = p
                
            p += 1  
            curr //= 10
         
        if k == -1: return num
        
        return num + 3 * 10 ** k