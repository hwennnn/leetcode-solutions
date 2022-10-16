class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        N = len(nums)
        n = N // 2
        
        counter = Counter(nums)
        
        for k, v in counter.items():
            if v == 1: return False
            
            n -= v // 2
        
        return n == 0