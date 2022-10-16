class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        parents = [-1] * n
        mmax = 1
        
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if 1 + dp[j] > dp[i]:
                        dp[i] = 1 + dp[j]
                        parents[i] = j
                        mmax = max(mmax, dp[i])
        
        maxi = dp.index(mmax)
        res = [nums[maxi]]
        while parents[maxi] != -1:
            maxi = parents[maxi]
            res.append(nums[maxi])
        
        return res
            