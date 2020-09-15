class Solution:
    def lengthOfLastWord(self, S: str) -> int:
        
        s = S.split()
        
        if not s: return 0
        
        return len(s[-1])