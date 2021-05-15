class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        M = 10 ** 9 + 7
        
        @cache
        def dp(d, target):
            if d == 0: return 1 if target == 0 else 0
            
            count = 0
            for k in range(max(0, target - f), target):
                count += dp(d - 1, k)
            
            return count
            
        return dp(d, target) % M