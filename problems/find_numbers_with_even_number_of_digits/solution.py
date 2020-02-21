class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        lst = [len(str(i)) for i in nums]

        return len([i for i in lst if i%2==0])