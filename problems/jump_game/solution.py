class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        maxJump = 0

        for i, x in enumerate(nums):
            if i > maxJump: return False
                
            maxJump = max(maxJump, i + x)
        
        return True
