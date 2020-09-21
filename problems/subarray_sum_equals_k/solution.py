class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = {0:1}
        s = 0
        res = 0
        
        for i,v in enumerate(nums):
            s += v
            res += prefix.get(s-k,0)
            prefix[s] = prefix.get(s,0) + 1
        
        return res
            