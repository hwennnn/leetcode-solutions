class Solution:
    def minimizeSet(self, d1: int, d2: int, a: int, b: int) -> int:
        left, right = 1, 10 ** 18
        l = lcm(d1, d2)
        
        def good(k):
            A = k - k // d1
            B = k - k // d2
            C = k - k // l
            
            return A >= a and B >= b and C >= a + b
            
        
        while left < right:
            mid = left + (right - left) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
            
        return left