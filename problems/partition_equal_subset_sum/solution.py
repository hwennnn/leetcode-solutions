class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total%2: return False # odd sum cannot be partitioned equally
        
        bits = 1
        for num in nums:
            bits |= bits << num
        
        return (bits >> total//2) & 1 == 1