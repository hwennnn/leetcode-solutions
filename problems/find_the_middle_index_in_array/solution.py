class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        for i,x in enumerate(nums):
            left = sum(nums[:i]) if i > 0 else 0
            right = sum(nums[i + 1:]) if i < len(nums) else 0

            if left == right:
                return i
        
        return -1