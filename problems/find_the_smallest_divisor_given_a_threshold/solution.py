class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def good(d):
            return sum(ceil(num/mid) for num in nums) <= threshold
    
        left, right = 1, 10**6
    
        while left < right:
            mid = (left+right)//2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left