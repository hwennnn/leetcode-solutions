class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        nums += nums
        
        for i, x in enumerate(nums):
            while stack and x > nums[stack[-1]]:
                res[stack.pop()] = x
            
            stack.append(i % n)
        
        return res