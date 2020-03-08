class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        check = [a == b for a,b in zip(nums,sorted(nums))]
        
        return 0 if all(check) else len(nums) - check.index(False) - check[::-1].index(False)