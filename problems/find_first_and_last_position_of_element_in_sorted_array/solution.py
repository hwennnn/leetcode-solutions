class Solution:
    
    def bs(self,nums,target):
        n = len(nums)
        low, high = 0, n-1
        first_pos = n
        while low <= high:
            mid = (low+high) // 2
            
            if nums[mid] >= target:
                first_pos = mid
                high = mid - 1
                
            else:
                low = mid + 1
    
        return first_pos
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        first = self.bs(nums,target)
        last = self.bs(nums,target+1)-1
        
        if first <= last:
            return [first,last]
        
        else:
            return [-1,-1]