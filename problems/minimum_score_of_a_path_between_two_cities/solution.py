class Solution:
    def minScore(self, N: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b, dist in roads:
            graph[a].append((b, dist))
            graph[b].append((a, dist))
            
        res = inf
        
        stack = [1]
        visited = set(stack)
        
        while stack:
            node = stack.pop()
            
            for nei, dist in graph[node]:
                res = min(res, dist)
                
                if nei in visited: continue
                
                visited.add(nei)
                stack.append(nei)
            
        return res