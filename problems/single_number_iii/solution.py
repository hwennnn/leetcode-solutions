class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bit = 0
        res = [0, 0]
        
        for x in nums:
            bit ^= x
        
        bit &= -bit
        
        for x in nums:
            if bit & x == 0:
                res[0] ^= x
            else:
                res[1] ^= x
        
        return res