class Solution:
    def minTimeToType(self, word: str) -> int:
        res = len(word)
        prev = 'a'
        
        for curr in word:
            val = (ord(curr) - ord(prev)) % 26
            prev = curr
            res += min(val, 26 - val)
        
        return res