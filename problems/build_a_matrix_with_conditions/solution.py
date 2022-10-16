class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        res = [[0] * k for _ in range(k)]
        
        def topoSort(A):
            adj = [[] for _ in range(k + 1)] 
            
            for a, b in A:
                adj[a].append(b)
            
            seen = [False] * (k + 1)
            order = []
            
            def dfs(x):
                if seen[x]: return
                
                seen[x] = True
                
                for nei in adj[x]:
                    if not seen[nei]:
                        dfs(nei)
                
                order.append(x)
            
            for x in range(1, k + 1):
                dfs(x)
            
            order.reverse()
            M = {j: i for i, j in enumerate(order)}
            
            if all(M[i] < M[j] for i, j in A):
                return order
            
            return None
        
        R = topoSort(rowConditions)
        C = topoSort(colConditions)
        
        if R is None or C is None:
            return []
        
        RM = {j : i for i, j in enumerate(R)}
        CM = {j : i for i, j in enumerate(C)}
        
        for x in range(1, k + 1):
            res[RM[x]][CM[x]] = x
            
        return res