def is_bipartite(graph, n):
    color = defaultdict(int)

    def go(x):
        for node in graph[x]:
            if node not in color:
                color[node] = -color[x]
                if not go(node):
                    return False
            else:
                if color[x] == color[node]:
                    return False

        return True

    for i in range(n):
        if i not in color:
            color[i] = 1
            if not go(i):
                return False

    return True
                

class Solution:
    def magnificentSets(self, N: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for a, b in edges:
            a -= 1
            b -= 1
            graph[a].append(b)
            graph[b].append(a)
        
        if not is_bipartite(graph, N): return -1
        
        groups = []
        grouped = set()
        
        for node in range(N):
            if node in grouped: continue
            
            group = set()
            stack = [node]
            
            while stack:
                curr = stack.pop()
                
                for nei in graph[curr]:
                    if nei in group: continue
                    group.add(nei)
                    stack.append(nei)
            
            groups.append(group)
            grouped |= group
        
        res = 0
        for group in groups:
            maxDepth = 0
            
            for start in group:
                depth = {}
                depth[start] = 0
                queue = deque([start])
                
                while queue:
                    node = queue.popleft()
                    
                    for nei in graph[node]:
                        if nei in depth: continue
                        
                        depth[nei] = depth[node] + 1
                        queue.append(nei)
                
                maxDepth = max(maxDepth, max(depth.values()))
                
            res += maxDepth + 1
        
        return res
        