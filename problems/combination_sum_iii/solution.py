class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def go(x, curr):
            if x == 10 or len(curr) == k:
                if len(curr) == k and sum(curr) == n:
                    res.append(curr)
                return
            
            go(x + 1, curr)
            go(x + 1, curr + [x])

        go(1, [])
        
        return res