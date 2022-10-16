class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        graph = defaultdict(list)
        res = 0
        
        for x, y in enumerate(parent):
            if y == -1 or s[x] == s[y]: continue
                
            graph[y].append(x)
            graph[x].append(y)
            
        @cache
        def go(node, prev):
            nonlocal res
            
            path = [1]
            
            for nei in graph[node]:
                if nei != prev:
                    path.append(go(nei, node) + 1)
            
            path.sort(reverse = 1)
            
            if len(path) == 1:
                res = max(res, path[0])
            else:
                res = max(res, path[0] + path[1] - 1)
            
            return path[0]

        for i in range(n):
            go(i, -1)
        
        return res