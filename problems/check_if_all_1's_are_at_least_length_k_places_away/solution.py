class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        stack = []
        
        for i,x in enumerate(nums):
            if x == 1:
                if stack and i - stack[-1] <= k:
                    return False
                
                stack.append(i)
        
        return True