class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = set()
        
        for char in s:
            if char in odd:
                odd.remove(char)
            else:
                odd.add(char)
        
        return len(s) - len(odd) + int(len(odd) > 0)
        