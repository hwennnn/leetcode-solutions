class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        visited = [False] * n
        p = collections.defaultdict(set)
        
        for x, y in edges:
            graph[y].append(x)
        
        def go(node):
            if visited[node]:
                return p[node]
            
            visited[node] = True
            parents = set()
            
            for parent in graph[node]:
                parents |= go(parent)
                parents.add(parent)
                    
            p[node] = parents
            return parents
        

        for node in range(n):
            if not visited[node]:
                go(node)
        
        res = []
        
        for i in range(n):
            res.append(sorted(list(p[i])))
        
        return res