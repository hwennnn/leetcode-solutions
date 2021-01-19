class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        
        res = ""
        
        def palindrome(i,j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            
            i += 1
            j -= 1

            return s[i:j+1]
        
        for i in range(len(s)-1):
            res = max(res, palindrome(i,i), palindrome(i, i+1), key = len)
        
        return res