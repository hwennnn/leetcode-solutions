class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        localMax = mmax = nums[0]
        partitionIndex = 0
        
        for i, x in enumerate(nums):
            if x < localMax:
                localMax = mmax
                partitionIndex = i
            else:
                mmax = max(mmax, x)
        
        return partitionIndex + 1