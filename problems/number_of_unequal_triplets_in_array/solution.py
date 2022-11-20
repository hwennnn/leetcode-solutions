class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        res += 1
        
        return res