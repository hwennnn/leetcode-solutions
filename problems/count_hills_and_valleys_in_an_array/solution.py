class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        
        for i in range(1, n - 1):
            if nums[i] == nums[i + 1]: continue
            left = i - 1
            right = i + 1
            
            while left >= 0 and nums[left] == nums[i]:
                left -= 1
            
            while right < n and nums[right] == nums[i]:
                right += 1
            
            if left >= 0 and right < n:
                l, r = nums[left], nums[right]
                if (nums[i] > l and nums[i] > r) or (nums[i] < l and nums[i] < r):
                    res += 1
        
        return res