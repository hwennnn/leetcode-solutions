class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        target = total // 2
        if total & 1: return False
        
        bits = 1
        
        for x in nums:
            bits |= (bits << x)
        
        return (bits & (1 << target)) > 0