class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = inf
        
        for num in nums:
            if num < first:
                first = num
            elif num > first and num < second:
                second = num
            elif num > second:
                return True
        
        return False