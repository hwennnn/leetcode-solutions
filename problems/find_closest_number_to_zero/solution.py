class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        m = float('inf')
        
        for x in nums:
            if abs(x) < abs(m):
                m = x
            elif abs(x) == abs(m):
                m = max(m, x)
        
        return m