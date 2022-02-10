class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        
        s = res = 0
        
        for x in nums:
            s += x
            
            if s - k in mp:
                res += mp[s - k]
            
            mp[s] += 1
        
        return res