class Solution:
    def maximumScore(self, nums: List[int], multi: List[int]) -> int:
        n, m = len(nums), len(multi)
        
        @lru_cache(1000)
        def dp(i, j):
            if j == m: return 0
            
            left = dp(i + 1, j + 1) + nums[i] * multi[j]
            right = dp(i, j + 1) + nums[n - (j - i) - 1] * multi[j]
            
            return max(left, right)
        
        return dp(0, 0)