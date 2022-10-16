class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set([x for x in nums if x != 0]))