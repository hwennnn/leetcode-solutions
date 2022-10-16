class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        res = 0
        R = set(restricted)
        visited = set()
        G = defaultdict(list)
        
        for a, b in edges:
            G[a].append(b)
            G[b].append(a)
        
        def dfs(node):
            visited.add(node)
            
            for nei in G[node]:
                if nei not in R and nei not in visited:
                    dfs(nei)
        
        dfs(0)
        return len(visited)