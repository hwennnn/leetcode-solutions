class Solution:
    def findLUSlength(self, words: List[str]) -> int:
        
        def getDuplicates():
            sset = set()
            duplicates = set()
            
            for word in words:
                if word in sset:
                    duplicates.add(word)
                sset.add(word)
            
            return duplicates
        
        def isSubsequence(a, b):
            i = j = 0
            
            while i < len(a) and j < len(b):
                if a[i] == b[j]: j += 1
                i += 1
            
            return j == len(b)
        
        words.sort(key = len, reverse = 1)
        duplicates = getDuplicates()
        if words[0] not in duplicates: return len(words[0])
        
        for i, word in enumerate(words):
            if word not in duplicates:
                for j in range(i):
                    if isSubsequence(words[j], words[i]): break
                    if j == i - 1: return len(word)
        
        return -1