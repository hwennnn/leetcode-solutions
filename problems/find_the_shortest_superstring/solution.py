class Solution:
    def shortestSuperstring(self, A):

        def overlap(p, n):
            l = min(len(p), len(n))
            for i in range(l - 1, -1, -1):
                if p[len(p) - i:] == n[:i]:
                    return i
            return 0
                    
        l = len(A)
        dist=[[0] * l for _ in range(l)]
        for i in range(l):
            for j in range(i + 1, l):
                dist[i][j] = overlap(A[i], A[j])
                dist[j][i] = overlap(A[j], A[i])
                # print(dist[i][j], dist[j][i])
                
        dp = [[0] * l for _ in range(1 << l)] # total overlap
        parent = [[None] * l for _ in range(1 << l)]
        
        for mask in range(1 << l):
            for bit in range(l):
                if (1 << bit) & mask:
                    pmask = mask ^ (1 << bit)
                    if pmask == 0: continue
                        
                    for pbit in range(l):
                        if (1 << pbit) & pmask:
                            if dp[pmask][pbit] + dist[pbit][bit] >= dp[mask][bit]:
                                dp[mask][bit] = dp[pmask][pbit] + dist[pbit][bit]
                                parent[mask][bit] = pbit
                                        
        mask = (1 << l) - 1
        bit = dp[mask].index(max(dp[mask]))
        idxList = []
        
        while bit is not None:
            idxList.append(bit)
            bit, mask = parent[mask][bit], mask ^ (1 << bit)
        idxList = idxList[::-1]
        
        res = []
        for i in range(len(idxList)):
            if i == 0:
                res.append(A[idxList[i]])
            else:
                res.append(A[idxList[i]][dist[idxList[i - 1]][idxList[i]]:])
                
        return ''.join(res)