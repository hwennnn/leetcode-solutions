class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" or haystack == needle: return 0
        
        n = len(needle)
        s = deque()
        
        for index, x in enumerate(haystack):
            if len(s) < n:
                s.append(x)
            
            if len(s) == n:
                word = "".join(s)
                if word == needle:
                    return index - n + 1
                
                s.popleft()
        
        return -1