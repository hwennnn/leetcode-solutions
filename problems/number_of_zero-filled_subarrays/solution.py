class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = curr = 0
        
        for x in nums:
            if x != 0:
                curr = 0
            else:
                curr += 1
                res += curr
        
        return res