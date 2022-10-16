class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        def getMask(word):
            mask = 0
            
            for x in word:
                mask |= (1 << (ord(x) - ord('a')))
            
            return mask
        
        masks = [getMask(word) for word in words]
        
        n = len(words)
        res = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        
        return res
        