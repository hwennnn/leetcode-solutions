class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        N = len(words)
        mp = {x : i for i, x in enumerate(words)}
        res = []
        
        for index, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]
                
                if prefix == prefix[::-1]:
                    suffixR = suffix[::-1]
                    if word != suffixR and suffixR in mp:
                        res.append([mp[suffixR], index])
                
                if j != len(word) and suffix == suffix[::-1]:
                    prefixR = prefix[::-1]
                    if word != prefixR and prefixR in mp:
                        res.append([index, mp[prefixR]])
                
        return res