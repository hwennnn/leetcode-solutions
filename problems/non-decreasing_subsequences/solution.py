class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = set()

        def go(index, curr):
            if index == N:
                if len(curr) >= 2:
                    res.add(tuple(curr))
                return

            go(index + 1, curr)
            if nums[index] >= curr[-1]:
                go(index + 1, curr + [nums[index]])

        for i in range(N):
            go(i + 1, [nums[i]])

        return res