class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0:-1}
        s = 0
        
        for i, x in enumerate(nums):
            s = (s + x) % k
            if s not in mp:
                mp[s] = i
            
            if i - mp[s] >= 2:
                return True
        
        return False