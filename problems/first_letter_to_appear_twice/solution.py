class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        
        for x in s:
            if x in seen:
                return x
            
            seen.add(x)