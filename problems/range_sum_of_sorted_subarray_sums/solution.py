class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        n = len(nums)
        arr = []
        M = int(1e9+7)
        
        for i in range(n):
            s = nums[i]
            for j in range(i+1,n):
                s += nums[j]
                nums.append(s)
        
        nums = sorted(nums)
        res = 0
        for i in range(left-1, right):
            res = (res + nums[i])%M
        
        return res%M