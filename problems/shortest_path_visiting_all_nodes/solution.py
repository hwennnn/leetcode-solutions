class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        visited = set()
        queue = collections.deque()
        full = (1 << n) - 1
        
        for i in range(n):
            mask = 1 << i
            visited.add((i, mask))
            queue.append((i, mask))
        
        level = 0
        
        while queue:
            n = len(queue)
            
            for _ in range(n):
                i, mask = queue.popleft()
                
                if mask == full: return level
                
                for nei in graph[i]:
                    new_mask = mask | (1 << nei)
                    
                    if (nei, new_mask) not in visited:
                        visited.add((nei, new_mask))
                        queue.append((nei, new_mask))
            
            level += 1
        
        return -1
            