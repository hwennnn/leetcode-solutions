class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp = collections.Counter(t)
        i = j = 0
        required = len(t)
        res = (float('inf'), 0)
        
        while j < len(s):
            if mp[s[j]] > 0:
                required -= 1
            
            mp[s[j]] -= 1
            
            while required == 0:
                length = j - i + 1
                
                if length < res[0]:
                    res = (length, i)
                
                if mp[s[i]] == 0:
                    required += 1
                
                mp[s[i]] += 1
                i += 1
            
            j += 1
        
        return "" if res[0] == float('inf') else s[res[1] : res[0] + res[1]]