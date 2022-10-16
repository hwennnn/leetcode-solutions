class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        M = 10 ** 9 + 7
        lcm = (a * b) // gcd(a, b)
        
        left, right = 0, min(a, b) * n
        
        while left < right:
            mid = left + (right - left) // 2
            
            if mid // a + mid // b - mid // lcm >= n:
                right = mid
            else:
                left = mid + 1
        
        return left % M