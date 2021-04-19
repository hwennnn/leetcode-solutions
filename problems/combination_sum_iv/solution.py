class Solution:
    def combinationSum4(self, nums, target):
        nums, combs = sorted(nums), [1] + [0] * (target)
        
        for i in range(target + 1):
            for num in nums:
                if num  > i: break
                combs[i] += combs[i - num]
                
        return combs[target]
        