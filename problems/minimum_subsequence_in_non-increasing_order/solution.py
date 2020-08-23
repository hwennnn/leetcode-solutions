class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        numSum = sum(nums) 
        resSum = 0 
        while resSum <= numSum:
            v = nums.pop()
            res.append(v)
            resSum += v
            numSum -= v
        return res   