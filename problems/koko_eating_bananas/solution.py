class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def good(k):
            need = 0
            
            for x in piles:
                need += ceil(x / k)
            
            return need <= h
        
        left, right = 1, max(piles)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left