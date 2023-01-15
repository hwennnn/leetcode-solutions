class Solution:
    def maxOutput(self, N: int, edges: List[List[int]], price: List[int]) -> int:
        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        @cache
        def go(node, prev):
            res = 0
            
            for adj in graph[node]:
                if adj != prev:
                    res = max(res, go(adj, node))
            
            return price[node] + res
        
        return max(go(node, -1) - price[node] for node in range(N))