class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        res = 1
        s, e = pairs[0]
        
        for start, end in pairs[1:]:
            if e >= start: continue
            s, e = start, end
            res += 1
        
        return res
        