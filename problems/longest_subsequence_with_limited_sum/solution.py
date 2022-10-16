class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        res = []
        prefix = list(accumulate(nums, initial = 0))

        for q in queries:

            index = bisect_right(prefix, q) - 1
            res.append(index)

        return res
            