class Solution:
    def validPalindrome(self, s: str) -> bool:
        valid = True
        n = len(s)
        i, j = 0, n - 1
        
        @cache
        def isPalindrome(i, j):
            nonlocal valid
            
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    if valid:
                        valid = False
                        return isPalindrome(i + 1, j) or isPalindrome(i, j - 1)
                    else:
                        return False
        
        
            return i >= j
        
        return isPalindrome(i, j)