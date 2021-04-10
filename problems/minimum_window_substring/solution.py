class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        mp = collections.Counter(t)
        
        n, start, end, required = len(s), 0, 0, len(t)
        res = (float('inf'), 0)
        
        while end < n:
            if mp[s[end]] > 0:
                required -= 1
            
            mp[s[end]] -= 1
            
            while required == 0:
                l = end - start + 1
                if l < res[0]:
                    res = (l, start)
                
                mp[s[start]] += 1
                if mp[s[start]] > 0:
                    required += 1
                
                start += 1
            
            end += 1
        
        return "" if res[0] == float('inf') else s[res[1]: res[0] + res[1]]