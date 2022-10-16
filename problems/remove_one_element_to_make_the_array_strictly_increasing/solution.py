class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        def isIncreasing(A):
            for i in range(1, len(A)):
                if A[i] <= A[i - 1]: return False
            
            return True
        
        for i in range(len(nums)):
            if isIncreasing(nums[:i] + nums[i + 1:]): return True
            
        return False