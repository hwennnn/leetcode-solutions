class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        
        mp = {0:-1}
        res = n = len(nums)
        c = 0
        
        for i,x in enumerate(nums):
            c = (c+x)%p
            mp[c] = i
            
            if (c - need)%p in mp:
                res = min(res, i - mp[(c - need) % p])
        
        return res if res != n else -1