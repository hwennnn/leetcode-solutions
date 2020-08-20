class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_less = float("inf")
        curr = 0
        
        for num in nums:
            curr += num
            min_less = min(min_less, curr)
                
        return -min_less+1 if min_less < 1 else 1
            
        
        