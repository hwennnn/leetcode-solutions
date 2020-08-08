class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        start = 1
        
        while (k > 0):
            if start not in arr:
                k -= 1
                if (k == 0):
                    return start
            
            start += 1
            
        return start
        
        
        
        
        
        
            
        
        
        