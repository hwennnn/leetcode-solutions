class Solution:
    def arraySign(self, nums: List[int]) -> int:
        x = 1
        
        for y in nums:
            x *= y
        
        return 1 if x > 0 else -1 if x < 0 else 0