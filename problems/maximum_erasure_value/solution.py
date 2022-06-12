class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = set()
        i = total = res = 0
        
        for j, x in enumerate(nums):
            while x in s:
                total -= nums[i]
                s.remove(nums[i])
                i += 1
                
            total += x
            s.add(x)
            res = max(res, total)
        
        return res