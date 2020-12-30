class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        def good(x):
            total = 0
            day = 1
            
            for w in weights:
                total += w
                if total > x:
                    total = w
                    day += 1
                
                if day > D:
                    return False
        
            return True
    
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left+right) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left