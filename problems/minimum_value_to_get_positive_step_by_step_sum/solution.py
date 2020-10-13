class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        c = 0
        m = float("inf")
        
        for num in nums:
            c += num
            m = min(m, c)
        
        return abs(m) + 1 if m < 0 else 1