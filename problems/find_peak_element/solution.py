class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            l, r = float(-inf) if mid - 1 < 0 else nums[mid - 1], float('-inf') if mid + 1 >= n else nums[mid + 1]
            
            if l < nums[mid] and nums[mid] > r:
                return mid
            elif nums[mid] < l:
                right = mid - 1
            else:
                left = mid + 1
        
        return left