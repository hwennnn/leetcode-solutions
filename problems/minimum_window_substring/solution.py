class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        mp = collections.Counter(t)
        
        start, end, required = 0, 0, len(t)
        res = (float(inf), 0)
        
        while end < len(s):
            if mp[s[end]] > 0:
                required -= 1
            
            mp[s[end]] -= 1
            
            while required == 0:
                length = end - start + 1
                if length < res[0]:
                    res = (length, start)
                
                mp[s[start]] += 1
                if mp[s[start]] > 0:
                    required += 1
                
                start += 1
            
            end += 1
            
        return "" if res[0] == float('inf') else s[res[1]: res[1] + res[0]]