class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        N = len(nums)
        M = 10 ** 9 + 7

        if sum(nums) < 2 * k: return 0

        @cache
        def dp(index, s):
            if index >= N: return 1

            skip = dp(index + 1, s)
            take = 0 if s + nums[index] >= k else dp(index + 1, s + nums[index])

            return (skip + take) % M
        
        return (pow(2, N, M) - 2 * dp(0, 0) + M) % M