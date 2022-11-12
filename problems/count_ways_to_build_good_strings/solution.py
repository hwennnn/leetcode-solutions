class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        M = 10 ** 9 + 7
        
        @cache
        def go(k):
            if k > high: return 0
            
            res = 0
            
            if low <= k <= high:
                res += 1
            
            return (res + go(k + zero) + go(k + one)) % M
        
        return go(0)
            
            