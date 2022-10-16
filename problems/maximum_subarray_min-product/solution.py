class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        M = 10 ** 9 + 7
        n = len(nums)
        res = 0
        
        prefix = [0]
        for x in nums:
            prefix.append(x + prefix[-1])
        
        l = [0] * n
        r = [0] * n
        stack = []
        
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            
            if stack:
                l[i] = stack[-1] + 1
            else:
                l[i] = 0
                
            stack.append(i)
        
        stack = []
        
        for i in reversed(range(n)):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            
            if stack:
                r[i] = stack[-1] - 1
            else:
                r[i] = n - 1
            
            stack.append(i)

        for i in range(n):
            res = max(res, nums[i] * (prefix[r[i] + 1] - prefix[l[i]]))
        
        return res % M