class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * 101
        res = [0] * n
        
        for c in nums:
            counts[c] += 1
            
        for i in range(1,101):
            counts[i] += counts[i-1]
            
        for i, num in enumerate(nums):
            if num != 0:
                res[i] = counts[num-1]
        
        return res