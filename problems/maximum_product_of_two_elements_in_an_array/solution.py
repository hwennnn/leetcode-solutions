class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        n = len(nums)
        count = 0
        
        for i in range(n):
            for j in range(i+1,n):
                count = max(count, (nums[i]-1)*(nums[j]-1))
        
        return count