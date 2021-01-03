class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        stack = []
        for x in nums:
            index = bisect_left(stack, x)
            if index == len(stack):
                stack.append(x)
            else:
                stack[index] = x
        
        return len(stack)