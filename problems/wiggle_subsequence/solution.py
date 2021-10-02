class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up = down = 1
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                down = up + 1
            elif nums[i] < nums[i - 1]:
                up = down + 1
        
        return max(up, down)
        