class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder = sum(nums) % p
        
        dp = {0:-1}
        n = res = len(nums)
        c = 0
        
        for i,v in enumerate(nums):
            c = (c+v)%p
            dp[c] = i
            
            if (c-remainder)%p in dp:
                res = min(res, i - dp[(c-remainder)%p])
        
        return res if res != n else -1
                