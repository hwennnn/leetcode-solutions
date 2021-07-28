class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        
        def dfs(target, index, path):
            if target < 0: return
            
            if target == 0:
                res.append(path)
                return
            
            for i in range(index, n):
                dfs(target - candidates[i], i, path + [candidates[i]])
        
        dfs(target, 0, [])
        
        return res