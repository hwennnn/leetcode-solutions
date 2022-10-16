class Solution:
    def maxScore(self, nums: List[int]) -> int:
        N = len(nums)
        G = [[0] * N for _ in range(N)]
        full_mask = (1 << N) - 1
        
        for x in range(N):
            for y in range(N):
                G[x][y] = gcd(nums[x], nums[y])
        
        @cache
        def go(index, mask):
            if mask == full_mask: return 0
            
            res = 0
            for x in range(N):
                if mask & (1 << x) > 0: continue
                for y in range(x + 1, N):
                    if mask & (1 << y) > 0: continue
                    res = max(res, index * G[x][y] + go(index + 1, mask | (1 << x) | (1 << y)))
                                  
            return res
        
        return go(1, 0)