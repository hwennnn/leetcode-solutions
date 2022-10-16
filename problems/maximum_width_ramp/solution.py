class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        res = 0
        
        for i in range(n - 1, -1, -1):
            if not stack or nums[i] > stack[-1][0]:
                stack.append((nums[i], i))
            else:
                j = stack[bisect.bisect(stack, (nums[i], i))][1]
                
                res = max(res, j - i)
        
        return res