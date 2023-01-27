class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        s = set(words)

        @cache
        def go(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in s and (suffix in s or go(suffix)):
                    return True
            
            return False
        
        res = []
        for word in words:
            if go(word):
                res.append(word)
        
        return res