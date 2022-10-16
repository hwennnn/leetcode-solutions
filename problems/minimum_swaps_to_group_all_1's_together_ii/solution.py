class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        nums = nums + nums
        prefix = [0]
        
        for x in nums:
            prefix.append(prefix[-1] + x)
        
        res = 0
        for i in range(n):
            res = max(res, prefix[i + ones] - prefix[i])
            
        return ones - res