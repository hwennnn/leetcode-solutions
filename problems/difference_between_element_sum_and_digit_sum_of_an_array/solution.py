class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        total = sum(nums)
        digits = 0
        
        for x in nums:
            while x > 0:
                digits += x % 10
                x //= 10
        
        return abs(total - digits)