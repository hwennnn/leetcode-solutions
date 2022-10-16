class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        visited = set([(i, 1 << i) for i in range(n)])
        queue = deque([(i, 1 << i, 0) for i in range(n)])
        full_mask = (1 << n) - 1
        
        while queue:
            node, mask, count = queue.popleft()
            
            if mask == full_mask:
                return count
            
            for nei in graph[node]:
                new_mask = mask | (1 << nei)
                if (nei, new_mask) in visited: continue
                visited.add((nei, new_mask))
                queue.append((nei, new_mask, count + 1))
        
        return -1