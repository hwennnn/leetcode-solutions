class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s, t = list(s), list(t)
        s1, s2 = {}, {}
        
        for i, (a,b) in enumerate(zip(s, t)):
            if a in s1:
                s[i] = s1[a]
            else:
                s[i] = s1[a] = len(s1)
            
            if b in s2:
                t[i] = s2[b]
            else:
                t[i] = s2[b] = len(s2)
        
        return s == t