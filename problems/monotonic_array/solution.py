class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        inc = dec = 0
        
        for i in range(n - 1):
            if nums[i] <= nums[i + 1]:
                inc += 1
            
            if nums[i] >= nums[i + 1]:
                dec += 1
        
        return inc == n - 1 or dec == n - 1