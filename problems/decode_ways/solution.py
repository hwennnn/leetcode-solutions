class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        @cache
        def go(i):
            if i == n: return 1
            
            count = 0
            
            if s[i] != '0':
                count += go(i + 1)
            
                if i + 1 < n and int(s[i: i + 2]) <= 26:
                    count += go(i + 2)
            
            return count
    
        return go(0)