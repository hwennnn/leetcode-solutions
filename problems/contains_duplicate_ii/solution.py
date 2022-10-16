class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        d = {}
        
        for i, n in enumerate(nums):
            
            if n not in d:
                d[n] = i
            
            else:
                if abs(d[n]-i) <= k:
                    return True
                
                d[n] = i
        
        return False
                
            