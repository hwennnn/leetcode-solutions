class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        
        left, right = 1, 10 ** 18
        
        def good(k):
            count = 0
            
            for x in piles:
                count += x // k + int(x % k != 0)
            
            return count <= h
                
        
        while left < right:
            mid = left + (right - left) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left