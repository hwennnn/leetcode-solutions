class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        N = len(parent)
        graph = defaultdict(list)
        res = 0

        for node, p in enumerate(parent):
            if p == -1 or s[node] == s[p]: continue

            graph[node].append(p)
            graph[p].append(node)
        
        @cache
        def go(node, prev):
            nonlocal res

            path = [1]

            for nei in graph[node]:
                if nei != prev:
                    path.append(1 + go(nei, node))
            
            path.sort(reverse = 1)

            if len(path) == 1:
                res = max(res, path[0])
            else:
                res = max(res, path[0] + path[1] - 1)

            return path[0]
        
        for node, p in enumerate(parent):
            go(node, p)
        
        return res