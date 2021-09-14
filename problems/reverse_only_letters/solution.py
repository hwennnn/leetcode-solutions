class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        
        i, j = 0, len(s) - 1
        
        while i < j:
            if not s[i].isalpha():
                i += 1
            elif not s[j].isalpha():
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        return "".join(s)