class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def good(x):
            return nums[x] >= target
    
        left, right = 0, len(nums)
        
        while left < right:
            mid = (left+right)//2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left