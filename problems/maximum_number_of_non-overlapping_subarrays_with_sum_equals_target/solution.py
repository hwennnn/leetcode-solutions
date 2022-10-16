class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
        d = {0:-1}
        last = -1
        s = res = 0
        
        for i,num in enumerate(nums):
            s += num
            if s - target in d and d[s-target] >= last:
                last = i
                res += 1
            
            d[s] = i
        
        return res