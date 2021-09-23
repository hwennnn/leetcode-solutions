class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = [0] * 26
        c2 = [0] * 26
        
        for c in s:
            c1[ord(c) - ord('a')] += 1
        
        for c in t:
            c2[ord(c) - ord('a')] += 1
        
        for i in range(26):
            if c1[i] != c2[i]: return False
        
        return True