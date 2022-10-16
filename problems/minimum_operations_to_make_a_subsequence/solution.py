class Solution:
    def LIS(self, nums):
        stack = []
        for x in nums:
            index = bisect_left(stack, x)
            if index == len(stack):
                stack.append(x)
            else:
                stack[index] = x
        
        return len(stack)
        
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        mp = {x:i for i,x in enumerate(target)}
        stack = []
        
        for x in arr:
            if x in mp:
                stack.append(mp[x])

        return len(target) - self.LIS(stack)
                