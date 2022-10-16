class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        n = len(s)
        res = 0
        
        while "01" in s:
            s = s.replace("01", "10")
            res += 1
        
        return res