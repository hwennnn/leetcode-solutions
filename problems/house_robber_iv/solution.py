class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        def good(mid):
            take = 0
            i = 0
            
            while i < N:
                if nums[i] <= mid:
                    take += 1
                    i += 2
                else:                
                    i += 1
            
            return take >= k
        
        left, right = min(nums), max(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left