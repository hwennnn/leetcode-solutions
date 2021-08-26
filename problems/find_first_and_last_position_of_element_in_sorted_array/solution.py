class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        def search(x):
            left, right = 0, n
            while left < right:
                mid = left + (right - left) // 2
                
                if nums[mid] >= x:
                    right = mid
                else:
                    left = mid + 1
            
            return left
        
        res = [search(target), search(target + 1) - 1]
        return [-1, -1] if res[0] >= n or nums[res[0]] != target else res