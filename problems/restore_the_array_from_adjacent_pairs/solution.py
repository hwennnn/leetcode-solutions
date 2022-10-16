class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        neigh = collections.defaultdict(list)
        res = []
        
        for a,b in adjacentPairs:
            neigh[a].append(b)
            neigh[b].append(a)
        
        for nei in neigh:
            if len(neigh[nei]) == 1:
                res.append(nei)
                res.append(neigh[nei][0])
                break
                
        while len(res) < len(adjacentPairs) + 1:
            prev, head = res[len(res)-2], res[-1]
            
            nei = neigh[head]
            
            if nei[0] == prev:
                res.append(nei[1])
            else:
                res.append(nei[0])
        
        return res