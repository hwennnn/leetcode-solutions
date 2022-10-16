class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        return min([abs(i - start) for i in range(len(nums)) if nums[i] == target])