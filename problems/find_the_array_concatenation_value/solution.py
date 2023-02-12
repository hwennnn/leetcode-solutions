class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        
        for i in range(N // 2):
            j = N - i - 1
            
            res += int(str(nums[i]) + str(nums[j]))
        
        if N % 2 == 1:
            res += nums[N // 2]
        
        return res