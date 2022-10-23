class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        N = len(nums)
        res = 0
        
        for i in range(N):
            g = 0

            for j in range(i, N):
                g = gcd(g, nums[j])
                
                if g == k:
                    res += 1
        
        return res
        