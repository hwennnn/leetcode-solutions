class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        
        for num in map(str,nums):
            res += (len(num) % 2 == 0)
        
        return res