class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        c = collections.Counter()
        curr = res = i = 0
        
        for j,x in enumerate(nums):
            curr += x
            c[x] += 1
            
            while c[x] >= 2:
                target = nums[i]
                c[target] -= 1
                curr -= target
                i += 1
            
            res = max(res, curr)
        
        return res
            