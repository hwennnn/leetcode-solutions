class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        N = len(nums)
        mod = defaultdict(int)
        
        for x in nums:
            k = x % space
            mod[k] += 1
        
        mmax = max(mod.values())
        res = inf
        for x in nums:
            k = x % space
            if mod[k] == mmax and x < res:
                res = x
        
        return res