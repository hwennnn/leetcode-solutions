class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def good(divisor):
            total = 0
            for num in nums:
                total += (num-1)//divisor + 1
            
            return total <= threshold
            
        left = 1
        right = 10 ** 8
        
        while left < right:
            mid = (left + right) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left