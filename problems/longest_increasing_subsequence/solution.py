class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        A = []
        
        for x in nums:
            index = bisect_left(A, x)
            
            if index < len(A):
                A[index] = x
            else:
                A.append(x)
        
        return len(A)