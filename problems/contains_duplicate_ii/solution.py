class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        d = {}
        
        for i,num in enumerate(nums):
            
            if num not in d:
                d[num] = i
            
            else:
                
                if i - d[num] <= k:
                    return True
                
                d[num] = i
            
        return False
            