class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        candidates.sort()
        
        def go(index, total, curr):
            if total == target:
                res.append(curr)
                return
            
            if index == n: return
            
            for j in range(index, n):
                if candidates[j] + total > target: break
                    
                go(j, total + candidates[j], curr + [candidates[j]])
        
        go(0, 0, [])
        
        return res