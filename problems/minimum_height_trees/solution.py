class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        
        adj = [set() for _ in range(n)]
        
        for e1,e2 in edges:
            adj[e1].add(e2)
            adj[e2].add(e1)
        
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1: newLeaves.append(j)
            leaves = newLeaves
        return leaves

        