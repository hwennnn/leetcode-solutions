class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        def go(curr, seen):
            nonlocal res
            
            if len(curr) == n:
                res.append(curr[:])
                return
            
            for i, x in enumerate(nums):
                if i in seen: continue
                seen.add(i)
                curr.append(x)
                go(curr, seen)
                seen.remove(i)
                curr.pop()
        
        go([], set())
        return res