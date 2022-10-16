class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        mp = {c:0 for c in "abc"}
        res = i = 0
        
        for j, c in enumerate(s):
            mp[c] += 1
            
            while all(mp.values()):
                mp[s[i]] -= 1
                i += 1
            
            res += i
        
        return res
        
        
        