class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        
        def go(index, curr, total):
            nonlocal res
            
            if total == target:
                res.append(curr)
                return
            
            if index == n:
                return
            
            for j in range(index, n):
                if total + candidates[j] <= target:
                    go(j, curr + [candidates[j]], total + candidates[j])
        
        go(0, [], 0)
        
        return res