class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        total = count = 0
        last = -1
        d = {0:-1}
        
        for i in range(n):
            
            total += nums[i]
            
            if total-target in d and d[total-target] >= last:
                count += 1
                last = i
                
            d[total] = i
        
        return count
                
            
            