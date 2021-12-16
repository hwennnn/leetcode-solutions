class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0: return []
        if n == 1: return [0]
        
        graph = collections.defaultdict(list)
        deg = [0] * n

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            deg[x] += 1
            deg[y] += 1
        
        queue = collections.deque()
        for i in range(n):
            if deg[i] == 1:
                queue.append(i)
                
        res = []
        while queue:
            res.clear()
            n = len(queue)
            
            for _ in range(n):
                x = queue.popleft()
                res.append(x)
                
                for nei in graph[x]:
                    deg[nei] -= 1
                    if deg[nei] == 1:
                        queue.append(nei)
        
        return res
        