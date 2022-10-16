class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(allowed)
        res = 0
        for w in words:
            s2 = set(w)
            check = False
            for c in s2:
                if c not in s:
                    check = True
                    break
            
            if not check: res += 1
        
        return res