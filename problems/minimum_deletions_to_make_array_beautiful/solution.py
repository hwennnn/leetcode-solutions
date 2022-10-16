class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        prev = None
        valid = 0
        
        for x in nums:
            if prev is not None:
                if x != prev:
                    prev = None
                    valid += 2
            else:
                prev = x
        
        return n - valid