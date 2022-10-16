class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        i, j = 0, len(x)-1
        
        while i < j and x[i] == x[j]:
            i += 1
            j -= 1
        
        return i >= j