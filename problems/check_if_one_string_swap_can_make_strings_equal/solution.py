class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        mp = [0] * 26
        n = len(s1)
        
        for a,b in zip(s1, s2):
            mp[ord(a) - ord('a')] += 1
            mp[ord(b) - ord('a')] -= 1
        
        for v in mp:
            if v != 0: return False
        
        diff = 0
        
        for i in range(n):
            if s1[i] != s2[i]:
                diff += 1
        
        return diff <= 2