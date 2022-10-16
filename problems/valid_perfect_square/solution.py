class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, 10 ** 18
        
        while left < right:
            mid = left + (right - left) // 2
            
            if mid * mid >= num:
                right = mid
            else:
                left = mid + 1
        
        return left * left == num