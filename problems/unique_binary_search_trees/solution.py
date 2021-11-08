class Solution:
    def numTrees(self, n: int) -> int:
        
        @cache
        def go(n):
            if n == 0: return 0
            if n == 1: return 1
            
            res = 0
            for head in range(n):
                res += max(1, go(head)) * max(1, go(n - head - 1))
            
            return res
        
        return go(n)