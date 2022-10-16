class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        res = ""
        
        for x in words:
            if x == x[::-1]:
                return x
        
        return res