class Solution:
    def reverseVowels(self, s: str) -> str:
        N = len(s)
        s = list(s)
        i, j = 0, N - 1

        while i < j:
            while i < j and s[i] not in "aeiouAEIOU":
                i += 1
            
            while i < j and s[j] not in "aeiouAEIOU":
                j -= 1
            
            s[i], s[j] = s[j], s[i]
            
            i += 1
            j -= 1
        
        return "".join(s)