class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        
        left, right = 1, max(nums)
        
        def good(k):
            count = 0
            
            for x in nums:
                count += ceil(x / k)
            
            return count <= threshold
        
        while left < right:
            mid = left + (right - left) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left