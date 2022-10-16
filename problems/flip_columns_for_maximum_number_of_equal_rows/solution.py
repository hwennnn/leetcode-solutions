class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        mp = collections.defaultdict(int)
        
        for r in matrix:
            A = []
            for c in r:
                A.append(r[0] ^ c)
            
            mp[tuple(A)] += 1
        
        return max(mp.values())