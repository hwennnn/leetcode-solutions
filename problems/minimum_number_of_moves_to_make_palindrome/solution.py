class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        n = len(s)
        s = list(s)
        start, end = 0, n - 1
        res = 0
        
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                i = end - 1
                
                while i > start and s[start] != s[i]:
                    i -= 1
                
                if start == i:
                    s[start], s[start + 1] = s[start + 1], s[start]
                    res += 1
                else:
                    while i < end:
                        s[i], s[i + 1] = s[i + 1], s[i]
                        i += 1
                        res += 1
                    
                    start += 1
                    end -= 1
        
        return res