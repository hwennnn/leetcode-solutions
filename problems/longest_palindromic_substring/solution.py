class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(i,j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            
            return s[i+1:j]
        
        res = ""
        for i in range(len(s)):
            res = max(res,helper(i,i), helper(i,i+1), key = len)
        
        return res