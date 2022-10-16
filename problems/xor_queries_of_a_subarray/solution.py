class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        prefix = [0]
        for x in arr:
            prefix.append(x ^ prefix[-1])
        
        for l,r in queries:
            res.append(prefix[l] ^ prefix[r+1])
        
        return res