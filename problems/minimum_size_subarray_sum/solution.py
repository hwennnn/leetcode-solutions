class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        i = ssum = 0
        
        for j,x in enumerate(nums):
            ssum += x
            
            while i <= j and ssum >= target:
                res = min(res, j - i + 1)
                ssum -= nums[i]
                i += 1
        
        return 0 if res == float('inf') else res