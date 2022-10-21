class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        
        for j, x in enumerate(nums):
            if x in mp and j - mp[x] <= k:
                return True
            
            mp[x] = j
        
        return False