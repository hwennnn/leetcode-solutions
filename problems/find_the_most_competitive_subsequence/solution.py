class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        
        for i,x in enumerate(nums):
            while res and len(res) + (n-i) > k and x < res[-1]:
                res.pop()
            
            if len(res) < k:
                res.append(x)
        
        return res
        