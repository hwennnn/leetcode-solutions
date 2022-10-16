class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        res, res1, res2 = [], [], []
        
        def f(word):
            count = [0] * 26
            for w in word:
                count[ord(w) - ord('a')] += 1

            for c in count:
                if c != 0: return c
            
            return -1
            
        for word in queries:
            res1.append(f(word))
        
        for word in words:
            res2.append(f(word))
        
        for x in res1:
            count = 0
            for y in res2:
                if y > x:
                    count += 1
            
            res.append(count)
        
        return res
        
        
            