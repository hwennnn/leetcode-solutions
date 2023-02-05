class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        N = len(words)
        prefix = [0]
        
        for x in words:
            ok = 1 if x[0] in "aeiou" and x[-1] in "aeiou" else 0
            
            prefix.append(prefix[-1] + ok)
            
        res = []
        for l, r in queries:
            res.append(prefix[r + 1] - prefix[l])
        
        return res