class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        res = s = i = 0
        n = len(nums)
        
        nums.sort()
        
        for j in range(n):
            s += nums[j]
            
            while nums[j] * (j - i + 1) - s > k:
                s -= nums[i]
                i += 1
            
            res = max(res, j - i + 1)
        
        return res