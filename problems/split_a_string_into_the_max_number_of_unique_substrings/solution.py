class Solution:
    def maxUniqueSplit(self, S: str) -> int:
        def backtrack(S, seen):
            res = 0
            for i in range(1, len(S)+1):
                c = S[:i]
                if c not in seen:
                    seen.add(c)
                    res = max(res, 1 + backtrack(S[i:], seen))
                    seen.remove(c)
            
            return res
        
        seen = set()
        return backtrack(S, seen)
                
        