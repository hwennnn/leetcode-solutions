class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        N = len(nums)
        res = 0
        minPos = maxPos = -1
        i = 0
        
        for j, x in enumerate(nums):
            if x == minK:
                minPos = j
                
            if x == maxK:
                maxPos = j
            
            if x > maxK or x < minK:
                i = j + 1
            
            res += max(0, min(minPos, maxPos) - i + 1)
        
        return res