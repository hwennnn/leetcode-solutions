class Solution:
    def countValidWords(self, sentence: str) -> int:
        res = 0
        
        for s in sentence.split():
            if any(c in s for c in "0123456789"):
                continue
            
            if s.count('-') > 1 or s[0] == '-' or s[-1] == '-':
                continue
            
            if '-' in s:
                index = s.index('-')
                if not s[index - 1].isalpha() or not s[index + 1].isalpha():
                    continue
            
            if sum(c in '!.,' for c in s) > 1:
                continue
            
            if any(c in '!.,' for c in s[:-1]):
                continue
            res += 1
            
        return res