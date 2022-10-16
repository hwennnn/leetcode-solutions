class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(list(set(nums)))
        n = len(nums)
        
        if nums[-1] <= k + n:
            return (k + n) * (k + n + 1) // 2 - sum(nums)
        
        left, right = 0, n - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] - mid > k:
                right = mid
            else:
                left = mid + 1
        
        return (left + k) * (left + k + 1) // 2 - sum(nums[:left])