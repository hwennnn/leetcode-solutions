class Solution:
    def customSortString(self, order: str, word: str) -> str:
        words = [0] * 26
        res = ''
        
        for w in word:
            words[ord(w) - ord('a')] += 1
        
        for w in order:
            ch = ord(w) - ord('a')
            res += w * words[ch]
            words[ch] = 0
        
        for i, count in enumerate(words):
            w = chr(i + ord('a'))
            if count > 0:
                res += w * count
                
        return res