class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        n = len(nums)
        
        for mask in range(1 << n):
            h = 0
            curr = []
            
            for j in range(n):
                if mask & (1 << j) > 0:
                    curr.append(nums[j])
                    h |= (1 << j)
            
            if h not in seen:
                res.append(curr)
                seen.add(h)
        
        return res