class Solution:
    def maxSubArray(self, a: List[int]) -> int:
        
        for i in range(1,len(a)):
            
            if a[i-1] > 0:
                a[i] += a[i-1]
        
        
        return max(a)