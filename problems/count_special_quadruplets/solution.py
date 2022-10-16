class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for z in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] == nums[z]:
                            res += 1
        
        return res