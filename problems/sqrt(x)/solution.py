class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        
        def good(v):
            return v*v <= x
        
        left, right = 0, x
        
        while left < right:
            mid = left + (right - left) // 2
            
            if good(mid):
                left = mid + 1
            else:
                right = mid
        
        return left - 1