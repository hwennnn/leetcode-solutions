class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = collections.defaultdict(int)
        mp[0] = 1
        
        curr = res = 0
        for num in nums:
            curr += num
            
            if curr - k in mp:
                res += mp[curr - k]
            
            mp[curr] += 1
        
        return res