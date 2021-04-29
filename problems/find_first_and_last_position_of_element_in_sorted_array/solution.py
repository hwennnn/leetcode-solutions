class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        def search(x):
            left, right = 0, n
            
            while left < right:
                mid = (left + right) // 2
                
                if nums[mid] >= x:
                    right = mid
                else:
                    left = mid + 1
            
            return left
        
        first, last = search(target), search(target + 1) - 1
        
        if first >= n or nums[first] != target: 
            return [-1, -1]
        
        return [first, last]