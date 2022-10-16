class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        res = 0
        
        for x in nums:
            res |= x
        
        return res
            