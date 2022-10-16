class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        left = right = 0
        curr = 1
        
        while right < n:
            curr *= nums[right]
            
            while left <= right and curr >= k:
                curr //= nums[left]
                left += 1
            
            res += right - left + 1
            right += 1
        
        return res