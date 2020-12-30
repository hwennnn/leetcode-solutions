class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def good(x):
            hours = 0
            for p in piles:
                r = ceil(p/x)
                hours += r
                if hours > H: return False
            
            return True
        
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left+right) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left