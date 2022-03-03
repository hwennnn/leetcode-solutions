class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        diff = 0
        
        for a, b in zip(s1, s2):
            if a != b:
                diff += 1
        
        return diff == 2 and Counter(s1) == Counter(s2)