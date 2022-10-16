class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        
        for mask in range(1 << n):
            count = 0
            for j in range(n):
                if mask >> j & 1:
                    count ^= nums[j]
                
            res += count
        
        return res