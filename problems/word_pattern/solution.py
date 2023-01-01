class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        def f(s):
            seen = {}
            res = []

            for x in s:
                if x not in seen:
                    seen[x] = len(seen)
                
                res.append(seen[x])
            
            return "".join(map(str, res))
        
        return f(pattern) == f(s.split())