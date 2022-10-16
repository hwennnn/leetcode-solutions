class Solution:
    def minimumBuckets(self, s: str) -> int:
        s = list(s)
        n = len(s)
        
        for i, x in enumerate(s):
            if x != "H": continue
            if i - 1 >= 0 and s[i - 1] == "B": continue
                
            if i + 1 < n and s[i + 1] == ".":
                s[i + 1] = "B"
            elif i - 1 >= 0 and s[i - 1] == ".":
                s[i - 1] = "B"
            else:
                return -1
            
        return s.count("B")