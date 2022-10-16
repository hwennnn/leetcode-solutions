class Solution:
    def countElements(self, nums: List[int]) -> int:
        c = set(nums)

        return sum([1 for x in nums if x+1 in nums])