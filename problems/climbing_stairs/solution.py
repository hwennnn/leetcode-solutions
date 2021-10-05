class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        
        return self.climbStairs(n - 2) + self.climbStairs(n - 1)