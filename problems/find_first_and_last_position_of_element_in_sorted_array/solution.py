class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        res = [bisect_left(nums, target), bisect_left(nums, target + 1) - 1]
        return [-1, -1] if res[0] >= n or nums[res[0]] != target else res