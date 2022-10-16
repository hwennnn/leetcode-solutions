class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        
        def isPalindrome(s, i, j):
            while i < j and s[i] == s[j]:
                i += 1
                j -= 1
            
            return i >= j
        
        def check(a, b):
            i, j = 0, len(a) - 1
            while i < j and a[i] == b[j]:
                i += 1
                j -= 1
            
            return isPalindrome(a,i,j) or isPalindrome(b,i,j)
        
        return check(a,b) or check(b,a)
            