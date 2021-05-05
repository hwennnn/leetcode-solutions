class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        
        left, right = 0, nums[0]
        res = 1
        
        while right < len(nums) - 1:
            res += 1
            nxt = max(i + nums[i] for i in range(left, right + 1))
            left, right = right, nxt
        
        return res