class Solution:
    def minimumTime(self, time: List[int], t: int) -> int:
        n = len(time)
        
        def good(x):
            count = 0
            
            for trip in time:
                count += x // trip
            
            return count >= t
        
        left, right = 1, t * max(time)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left