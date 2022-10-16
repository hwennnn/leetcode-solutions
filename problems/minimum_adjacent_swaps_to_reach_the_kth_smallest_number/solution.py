class Solution:
    def getMinSwaps(self, nums: str, k: int) -> int:
        n = len(nums)
        
        def nextPermutation(nums):
            i = n - 1
            while i > 0 and nums[i-1] >= nums[i]:
                i -= 1
                
            j = i
            while j < n and nums[i-1] < nums[j]:
                j += 1
                
            nums[i-1], nums[j-1] = nums[j-1], nums[i-1]
            nums[i:] = nums[i:][::-1]
            
            return nums
        
        swapped = list(nums)
        for _ in range(k):
            swapped = nextPermutation(swapped)
        
        res = 0
        for i in range(n):
            j = i
            
            while j < n and swapped[j] != nums[i]: j += 1
            
            while i < j:
                swapped[j], swapped[j - 1] = swapped[j - 1], swapped[j]
                res += 1
                j -= 1
        
        return res
                