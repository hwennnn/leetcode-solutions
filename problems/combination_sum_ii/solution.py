class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        candidates.sort()
        
        def dfs(target, index, path):
            if target < 0: return
            
            if target == 0:
                res.append(path)
                return
            
            for i in range(index, n):
                if i > index and candidates[i] == candidates[i - 1]: continue
                dfs(target - candidates[i], i + 1, path + [candidates[i]])
        
        dfs(target, 0, [])
        
        return res