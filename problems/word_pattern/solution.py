class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        def generate(s):
            seen = {}
            res = []
            
            for word in s:
                if word not in seen:
                    seen[word] = len(seen)
                    
                res.append(seen[word])
            
            return "".join(map(str, res))
        
        return generate(pattern) == generate(s.split())
            