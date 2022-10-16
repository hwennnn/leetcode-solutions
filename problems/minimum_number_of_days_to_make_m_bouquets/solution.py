class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        n = len(bloomDay)
        if n < m*k: return -1
        
        def good(day):
            flower = bonquet = 0
            
            for i,x in enumerate(bloomDay):
                if x > day: flower = 0
                else:
                    flower += 1
                    if flower == k:
                        flower = 0
                        bonquet += 1
                
                if bonquet == m: break
            
                    
            return bonquet >= m
        
        left, right = min(bloomDay), max(bloomDay)
        
        while left < right:
            mid = (left+right)//2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left