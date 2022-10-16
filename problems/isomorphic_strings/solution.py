class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        def construct(s):
            s = list(s)
            mp = {}
            res = ""
            
            for i, x in enumerate(s):
                if x not in mp:
                    mp[x] = len(mp)
                s[i] = mp[x]
                
            return s
        
        return construct(s) == construct(t)
            