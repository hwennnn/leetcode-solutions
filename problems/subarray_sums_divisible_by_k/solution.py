class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp = collections.defaultdict(int)
        mp[0] = 1
        res = s = 0
        
        for x in nums:
            s = (s + x) % k
            
            res += mp[s]
            
            mp[s] += 1
            
        return res