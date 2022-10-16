class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        right, prefixMax = -1, nums[0]
        
        for i in range(1, n):
            if nums[i] < prefixMax:
                right = i
            else:
                prefixMax = nums[i]
        
        if right == -1: return 0
        
        left, suffixSmall = n - 1, nums[-1]
        
        for i in range(n - 2, -1, -1):
            if nums[i] > suffixSmall:
                left = i
            else:
                suffixSmall = nums[i]
        
        return right - left + 1