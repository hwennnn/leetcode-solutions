class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False
        
        target = total // 2
        
        s = 1
        
        for x in nums:
            s |= (s << x)
        
        return (s & (1 << target)) != 0