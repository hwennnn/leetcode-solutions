class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        def backtrack(curr, mask):
            if len(curr) == n:
                res.append(curr)
                return
            
            for i in range(n):
                if (mask >> i) & 1:
                    backtrack(curr + [nums[i]], mask ^ (1 << i))
                    
        backtrack([], (1 << n) - 1)
        return res