class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        s = set()
        
        for i in range(N // 2):
            s.add((nums[i] + nums[~i]) / 2)
        
        return len(s)